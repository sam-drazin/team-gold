import simplejson as json
import pymysql

db = pymysql.connect(
    host='hedge-fund-13f-filings.cuqh3juyttmr.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    db='HF_13f_filings')
c = db.cursor()

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
for i in json_stocks:
    # print(i)
    i_cik = i[1]
    i_rnk = i[6]
    #print(str(i_cik) + " " + str(i_rnk))
    fund_dict[i_cik] = i_rnk
keys = list(fund_dict)

fund_to_stocks = {}
for i in fund_dict:
    a = 0
    for j in range(0, fund_dict[i]):
        a+=j
    for k in range(0,a):
        print(json_stocks[k])


# #make a dictionary: fund -> list of tuples -> (stocks in the fund, percentage up or down since last quarter) 
# a = 1
# for i in range(len(json_stocks)):
#     print("this is the " + str(a) + "th part of json_stocks")
#     print(json_stocks[i])
#     a += 1


#Stage1 putting the funds/stocks in a dictionary
# prereqs:
# 1) declare a variable for total # of stocks in current fund. Call it cur_total_stocks
# 2) declare a variable for name of which fund we're on. Call it cur_fund_cik
# 3) declare a variable for which index we're on in fund_dict. Call it index_in_fd
#  
# step 1: get the number of stocks for the fund. 
#       base case: pull this from the [0] in fund_dict
#       as it loops: 
#           a) set cur_total_stocks to rank from fund_dict[index_in_fd]
#           b) set cur_fund_cik to i
#           increase index_in_fd by 1
 

    