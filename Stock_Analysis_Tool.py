#This program downloads the data from the last 2 years of 13F-HR filings from a pre-selected group of hedge funds.
#Each funds filings will be saved in a .json file contained in a folder called 'filings' in the working directory.

# 
# Currently up to the point where I am trying to put multiple filings into one faketable in sql. 
# Command line is giving this error:
#
#
from sec_api import QueryApi
import simplejson as json
import pymysql,os,requests,operator




db = pymysql.connect(
    host='hedge-fund-13f-filings.cuqh3juyttmr.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    db='HF_13f_filings')
c = db.cursor()


# queryApi = QueryApi(api_key="2cbca106dd8006615cc5360d3752653aca521d4ba07b3f4b3316961b93eab3d2") #Your API Key that can be obtained from the sec-api site

all_filings = []

fund_to_cik = [ 
    {"Fund" : "Citadel", "cik" : "1423053"},
    {"Fund" : "ExodusPoint", "cik" : "1736225"},
    {"Fund" : "Millburn RidgeField", "cik" : "1294571"},
    {"Fund" : "Point72", "cik" : "1603466"},
    {"Fund" : "Light Street", "cik" : "1569049"},
    {"Fund" : "Toscafund", "cik" : "1439289"},
    {"Fund" : "Valinor", "cik" : "1401388"},
    {"Fund" : "Matrix Capital Co.", "cik" : "1410830"},
    {"Fund" : "Discovery Capital", "cik" : "1389507"},
    {"Fund" : "Healthcor", "cik" : "1343781"},
    {"Fund" : "Bridgewater", "cik" : "1350694"},
    {"Fund" : "Impala", "cik" : "1317679"},
    {"Fund" : "Marshall Wace", "cik" : "1318757"},
    {"Fund" : "Lone Pine", "cik" : "1061165"},
    {"Fund" : "Intrepid Capital", "cik" : "1092838"},
    {"Fund" : "Sun Valley Gold", "cik" : "1280493"},
    {"Fund" : "Millennium", "cik" : "1273087"},
    {"Fund" : "Balyasny", "cik" : "1218710"},
    {"Fund" : "Bridger", "cik" : "1166309"},
    {"Fund" : "Tiger Global", "cik" : "1167483"},
    {"Fund" : "Second Curve", "cik" : "1136704"},
    {"Fund" : "Coatue", "cik" : "1135730"},
    {"Fund" : "Joho", "cik" : "1106500"},
    {"Fund" : "Schoenfeld", "cik" : "1040198"},
    {"Fund" : "Third Point", "cik" : "1040273"},
    {"Fund" : "Viking Global", "cik" : "1103804"},
    {"Fund" : "Soros Fund", "cik" : "1029160"},
    {"Fund" : "Maverick", "cik" : "934639"},
    {"Fund" : "DE Shaw", "cik" : "1009207"}
]
cik = [
    "1423053",
    "1736225",
    "1294571",
    "1603466",
    "1569049",
    "1439289",
    "1401388",
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
    "1029160",
    "934639",
    "1009207"
]



# CREATE TABLE
# sql = '''
# create table FakeTableWithAllHoldings (
# filingDate text,
# shares int,
# value int,
# cusip varchar(255),
# nameOfIssuer text,
# CIK int
# )
# '''
# c.execute(sql)


# for a in range(len(cik)):
#     print("now on fund number: " + str(a+1))
#     fund_cik = cik[a]
#     query = {
#         "query": {
#             "query_string": {
#                 "query": "cik %s AND formType:13F-HR" % fund_cik
#             }
#         },
#         "from": "0",
#         "sort": [{"filedAt": {"order": "desc"}}]
#     }
#     print(query.get('query').get('query_string').get('query') + "fund_cik is: " + fund_cik)
    
#     filings = queryApi.get_filings(query)
#     #These next couple lines are to prevent double filings with a different fund which was occuring amongst a few of the funds
#     set_size = 0
#     for i in filings.get('filings'):
#         if(set_size > 4):
#             break
#         set_size += 1
#         if(i.get('cik') != fund_cik):
#             continue
#         if(i.get('holdings') == None):
#                #print("skipped")
#             continue
#         if(i.get('periodOfReport') == None):
#             continue
#         filingDate = i.get('periodOfReport')
        
#         cik_of_fund = i.get('cik')
        
#         fund_name = i.get('companyNameLong')
#         print("filingDate: " + str(filingDate) + " fund_name: " + str(fund_name) + " cik: " + str(cik[a]))
#         #print(i.get('holdings'))

#         for j in i.get('holdings'):
#             all_filings.append(j)
#             s = j.get('shrsOrPrnAmt')
#             shares = str(s.get('sshPrnamt'))        
#             value = str(j.get('value'))                    
#             cusip = str(j.get('cusip'))        
#             nameOfIssuer = str(j.get('nameOfIssuer'))
#             print("Shares: " + shares + " value: " + value + " cusip: " + cusip + " nameOfIssuer: " + nameOfIssuer + " filing Date: " + filingDate + " cik: " + cik[a]) 
#             sql = "INSERT INTO FakeTableWithAllHoldings (cusip, nameOfIssuer, shares, value, filingDate, CIK) VALUES (%s, %s, %s, %s, %s, %s)" 
#             c.execute(sql,(cusip, nameOfIssuer, shares, value, filingDate,cik[a]))
#             db.commit()     
#     print("finished with fund: " + fund_name)
# print("Here is a collection of all the filings:")
# print(all_filings)

create_temp_table = '''
Create temporary table sumValues
select sum(valueInDollars) as valSum,cik,cusip,filingDate,nameOfIssuer
from All_Holdings_Raw_Data
where filingDate = "2021-03-31"
group by filingDate, cik, cusip;
'''

get_top_25 = '''

SELECT * 
FROM (
    SELECT s.valSum,s.cik,s.cusip,s.nameOfIssuer,s.filingDate,f.name, RANK() OVER (PARTITION BY s.CIK, s.filingDate ORDER BY s.valSum desc,s.nameOfIssuer) AS rnk
    FROM sumValues s, HF_Data f 
    Where s.CIK = f.CIK
    order by s.cik, rnk
) AS x
WHERE rnk <= 25;
'''
drop_temp_table = "drop temporary table sumValues;"
c.execute(create_temp_table)
c.execute(get_top_25)
data=c.fetchall()
c.execute(drop_temp_table)

json_stocks_string = json.dumps(data)
json_stocks = json.loads(json_stocks_string)

fund_dict = {}
stock_dict = {}
best_stocks = []

for i in json_stocks:
    print(i)
    i_cik = i[1]
    i_rnk = i[6]
    print(str(i_cik) + " " + str(i_rnk))
    fund_dict[i_cik] = i_rnk
keys = list(fund_dict)
#print(len(keys))
for i in json_stocks:
    i_cusip = i[2]
    stock_dict[i_cusip] = 0
for i in json_stocks:
    i_cusip = i[2]
    i_nameOfIssuer = i[3]
    name_and_cusip = (i_cusip,i_nameOfIssuer)
    i_rnk = i[6]
    divisor = fund_dict[i[1]]
    new_rank = int(i_rnk)/int(divisor)
    # this is going to skew the rating by 0.04 because the rankings go from 1-25, which when divided by the max of 25, is .04-1
    if(new_rank <= 0.2):
        new_rank = 5
    elif(0.2 < new_rank <= 0.4):
        new_rank = 4
    elif(0.4 < new_rank <= 0.6):
        new_rank = 3
    elif(0.6 < new_rank <= 0.8):
        new_rank = 2
    elif(0.8 < new_rank <= 1):
        new_rank = 1
    # print("this is the stock name and cusip: " + str(name_and_cusip))
    stock_dict[i_cusip] += new_rank
    #print(str(stock_dict[cusip]))
stocks = list(stock_dict)
for i in range(len(stock_dict)):
    stock_dict[stocks[i]] /= 27
    #print(stocks[i] + " " + str(stock_dict[stocks[i]]))
stock_dict = dict(sorted(stock_dict.items(), key=operator.itemgetter(1),reverse=True))
stocks = list(stock_dict)
for i in range(1,11):
    best_stocks.append(stocks[i])
#print(best_stocks)

return_list = []

#print(list_of_top_11[1])

def validate_nine_chars(cusip):
     if(cusip == "46090"):
         return "46090E103"
     zero = 0
     while(len(cusip) < 9):
         cusip = str(zero) + cusip
     #print("this is the full 9-digit cusip: " + cusip)
     return cusip

# this is for transforming the CUSIP into a stock ticker.
for i in range(len(best_stocks)):
    cusip = validate_nine_chars(best_stocks[i])   
    urlBeg = 'https://finnhub.io/api/v1/search?q='
    urlEnd = '&token=c3rnfbaad3i88nmm0ai0'
    fullUrl = str(urlBeg)+str(cusip)+str(urlEnd)
    r = requests.get(fullUrl)
    f = r.json()
    #print(f)
    temp = f.get('result')
    temp2 = temp[0].get('symbol')
    return_list.append(temp2)

print(return_list)

c.close()
