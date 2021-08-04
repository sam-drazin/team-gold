# IMPORTS FOR CHECKING IF DB IS UP TO DATE
import datetime as dt 
#
# IMPORTS FOR EDGAR
from sec_api import QueryApi
# IMPORTS FOR SQL DB CONNECTION
import pymysql

import Import_Data_To_DB as import_data

# CHANGE FIELDS TO YOUR OWN PERSONAL FIELDS
db = pymysql.connect(
  host = 'your database hosting site',
  user = 'your username',
  password = 'your password',
  db = 'Name of the database to which you are connecting'
)
c = db.cursor()

#OUR WORKING DB
# db = pymysql.connect(
#     host='hedge-fund-13f-filings.cuqh3juyttmr.us-east-1.rds.amazonaws.com',
#     user='admin',
#     password='12345678',
#     db='HF_13f_filings')
# c = db.cursor()

# CHANGE TABLE NAME TO WHAT YOU WANT THE TABLE TO BE CALLED
Your_Table_Name = "insert name here"

# CREATE TABLE
sql = '''
create table %s (
filingDate text,
shares int,
value int,
cusip varchar(255),
nameOfIssuer text,
CIK int
)
''' % Your_Table_Name
c.execute(sql)

import_data.run_import(5)