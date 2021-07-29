#This program downloads the data from the last 2 years of 13F-HR filings from a pre-selected group of hedge funds.
#Each funds filings will be saved in a .json file contained in a folder called 'filings' in the working directory.

# 
# Currently up to the point where I am trying to put multiple filings into one faketable in sql. 
# Command line is giving this error:
#
#
from sec_api import QueryApi
import pymysql,json,os




db = pymysql.connect(
    host='hedge-fund-13f-filings.cuqh3juyttmr.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    db='HF_13f_filings')
c = db.cursor()


queryApi = QueryApi(api_key="08326206184745c3bfd692d2ab3c92721a7329ba0445e95b59a0979296dd1a3f") #Your API Key that can be obtained from the sec-api site

all_filings = []

citadel = [ {"Fund" : "Citadel", "cik" : "1423053"},
    {"Fund" : "ExodusPoint", "cik" : "1736225"},
    {"Fund" : "Millburn RidgeField", "cik" : "1294571"},
    {"Fund" : "Point72", "cik" : "1603466"},
    {"Fund" : "Light Street", "cik" : "1569049"},
    "1439289",]
cik = [
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


# # CREATE TABLE
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


for a in range(len(cik)):
    print("now on fund number: " + str(a+1))
    fund_cik = cik[a]
    query = {
        "query": {
            "query_string": {
                "query": "cik %s AND formType:13F-HR" % fund_cik
            }
        },
        "from": "0",
        "sort": [{"filedAt": {"order": "desc"}}]
    }


    filings = queryApi.get_filings(query)
    #These next couple lines are to prevent double filings with a different fund which was occuring amongst a few of the funds
    longName = filings.get('filings')[0].get('companyNameLong')
    set_size = 0
    for i in filings.get('filings'):
        if(set_size > 4):
            break
        set_size += 1
        if(i.get('companyNameLong') != longName):
            continue
        if(i.get('holdings') == None):
               #print("skipped")
            continue
        if(i.get('periodOfReport') == None):
            continue
        filingDate = i.get('periodOfReport')
        cik = i.get('cik')
        fund_name = i.get('companyNameLong')
        print("filingDate: " + filingDate + " fund_name: " + fund_name + " cik: " + cik)
        #print(i.get('holdings'))

        for j in i.get('holdings'):
            s = j.get('shrsOrPrnAmt')
            shares = str(s.get('sshPrnamt'))        
            value = str(j.get('value'))                    
            cusip = str(j.get('cusip'))        
            nameOfIssuer = str(j.get('nameOfIssuer'))

            #print("Shares: " + shares + " value: " + value + " cusip: " + cusip + " nameOfIssuer: " + nameOfIssuer + " filing Date: " + filingDate + " cik: " + cik) 
            sql = "INSERT INTO FakeTableWithAllHoldings (cusip, nameOfIssuer, shares, value, filingDate, CIK) VALUES (%s, %s, %s, %s, %s, %s)" 
            c.execute(sql,(cusip, nameOfIssuer, shares, value, filingDate,cik))
            db.commit()     
    print("finished with fund: " + fund_name)



#This was for manually importing each fund by its hardcoded query


        
# print("finished second fund") 
    
    
# This was for manually creating queries per fund by hardcoding their cik in.


# query2 = {
#     "query": {
#         "query_string": {
#             "query": "cik 1061165 AND formType:13F-HR"
#         }
#     },
#     "from": "0",
#     "sort": [{"filedAt": {"order": "desc"}}]
# }
    
    
    
    
    
    
    
    
# for i in range(len(cik)):
#     query = {
#         "query": {
#             "query_string": {
#                 "query": "cik %s AND formType:13F-HR" % cik[i].get('cik')
#             }
#         },
#         "from": "0",
#         "sort": [{"filedAt": {"order": "desc"}}]
#     }
#     filings = queryApi.get_filings(query)
#     # print(filings)
#     all_filings.append(filings)
#     print(cik[i].get('Fund'))
    # if not os.path.exists("filings"):
    #     os.mkdir("filings")
    # with open('filings/Citadel.json', 'w', encoding='utf-8') as f:
    #     json.dump(filings, f, ensure_ascii=False, indent=4)


# #Citadel
# query1 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }







# #ExodusPoint
# query2 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query2)
# with open('filings/ExodusPoint.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Millburn RidgeField
# query3 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query3)
# with open('filings/Millburn_Ridgefield.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Point72
# query4 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query4)
# with open('filings/Point72.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Light Street
# query5 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query5)
# with open('filings/Light_Street.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Toscafund
# query6 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query6)
# with open('filings/Toscafund.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Valinor
# query7 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query7)
# with open('filings/Valinor.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Matrix Capital Co.
# query8 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query8)
# with open('filings/Matrix_Capital_Co.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Discovery Capital
# query9 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query9)
# with open('filings/Discovery_Capital.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Healthcor
# query10 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query10)
# with open('filings/Healthcor.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Bridgewater
# query11 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query11)
# with open('filings/Bridgewater.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Impala
# query12 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query12)
# with open('filings/Impala.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Marshall Wace
# query13 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query13)
# with open('filings/Marshall_Wace.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Lone Pine
# query14 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query14)
# with open('filings/Lone_Pine.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Intrepid Capital
# query15 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query15)
# with open('filings/Intrepid_Capital.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Sun Valley Gold
# query16 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query16)
# with open('filings/Sun_Valley_Gold.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Millennium
# query17 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query17)
# with open('filings/Millennium.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Balyasny
# query18 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query18)
# with open('filings/Balyasny.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Bridger
# query19 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query19)
# with open('filings/Bridger.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Tiger Global
# query20 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query20)
# with open('filings/Tiger_Global.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Second Curve
# query21 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query21)
# with open('filings/Second_Curve.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Coatue
# query22 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query22)
# with open('filings/Coatue.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Joho
# query23 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query23)
# with open('filings/Joho.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Schoenfeld
# query24 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query24)
# with open('filings/Schoenfeld.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Third Point
# query25 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query25)
# with open('filings/Third_Point.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Viking Global
# query26 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query26)
# with open('filings/Viking_Global.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Soros Fund
# query27 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query27)
# with open('filings/Soros_Fund.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #Maverick
# query28 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query28)
# with open('filings/Maverick.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)

# #DE Shaw
# query29 = {
#     "query": {
#         "query_string": {
#             "query": "cik:  AND formType:13F-HR" 
#         }
#     },
#     "from": "0",
#     "size": "12", 
#     "sort": [{ "filedAt": { "order": "desc" } }]
# }

# filings = queryApi.get_filings(query29)
# with open('filings/DE_Shaw.json', 'w', encoding='utf-8') as f:
#     json.dump(filings, f, ensure_ascii=False, indent=4)