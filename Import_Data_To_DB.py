#This function queries the hedge fund data from a list of CIKs
#Downloads the data as .json files (one per fund), reads the data from the files and puts it into the database.
#@param number_of_quarters is the number of most recent quarters for which data should be pulled.
def run_import(number_of_quarters):
    # IMPORTS FOR CHECKING IF DB IS UP TO DATE
    import datetime as dt 
    #
    # IMPORTS FOR EDGAR
    from sec_api import QueryApi
    # IMPORTS FOR SQL DB CONNECTION
    import pymysql

    # CHANGE FIELDS TO YOUR OWN PERSONAL FIELDS
    # db = pymysql.connect(
    #   host = 'your database hosting site',
    #   user = 'your username',
    #   password = 'your password',
    #   db = 'Name of the database you are connecting to'
    # )
    # c = db.cursor()

    #OUR WORKING DB
    db = pymysql.connect(
        host='hedge-fund-13f-filings.cuqh3juyttmr.us-east-1.rds.amazonaws.com',
        user='admin',
        password='12345678',
        db='HF_13f_filings')
    c = db.cursor()

    #ENTER YOUR OWN QUERY API
    queryApi = QueryApi(api_key="2cbca106dd8006615cc5360d3752653aca521d4ba07b3f4b3316961b93eab3d2") 
    
    cik = [
        "1401388",
        "1029160",
        "1423053",
        "1736225",
        "1294571",
        "1603466",
        "1569049",
        "1439289",
        "1410830",
        "1389507",
        "1343781",
        "1350694",
        "1317679",
        "1318757",
        "1061165",
        "1092838",
        "1280493",
        "1273087",
        "1218710",
        "1166309",
        "1167483",
        "1136704",
        "1135730",
        "1106500",
        "1040198",
        "1040273",
        "1103804",
        "934639",
        "1009207"
    ]

    all_filings = []

    for a in range(len(cik)):

        #Download the data for the funds identified by each CIK
        fund_cik = cik[a]
        print("Starting with fund: " + str(fund_cik))
        query = {
            "query": {
                "query_string": {
                    "query": "cik: "+ str(fund_cik) + " AND formType:13F-HR"
                }
            },
            "from": "0",
            "size": str(number_of_quarters),
            "sort": [{"filedAt": {"order": "desc"}}]
        } #% str(number_of_quarters)
        print(query.get('query').get('query_string').get('query') + "fund_cik is: " + str(fund_cik))

        filings = queryApi.get_filings(query)
        #These next few lines are to prevent double filings with a different fund which was occuring amongst a few of the funds
        set_size = 0
        for i in filings.get('filings'):
            if(set_size > 4):
                break
            set_size += 1
            if(i.get('cik') != fund_cik):
                continue
            if(i.get('holdings') == None):
                continue
            if(i.get('periodOfReport') == None):
                continue
            
            #Input the downloaded data into the database.
            filingDate = i.get('periodOfReport')        
            cik_of_fund = i.get('cik')
            fund_name = i.get('companyNameLong')
            for j in i.get('holdings'):
                all_filings.append(j)
                s = j.get('shrsOrPrnAmt')
                shares = str(s.get('sshPrnamt'))        
                value = str(j.get('value'))                    
                cusip = str(j.get('cusip'))        
                nameOfIssuer = str(j.get('nameOfIssuer'))
                sql = "INSERT INTO All_Holdings_Raw_Data (cusip, nameOfIssuer, shares, value, filingDate, CIK) VALUES (%s, %s, %s, %s, %s, %s)" 
                c.execute(sql,(cusip, nameOfIssuer, shares, value, filingDate,cik[a]))
                db.commit()     
        print("finished with fund: " + fund_name)