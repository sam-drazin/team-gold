#This program downloads the data from the last 2 years of 13F-HR filings from a pre-selected group of hedge funds.
#Each funds filings will be saved in a .json file contained in a folder called 'filings' in the working directory.

# 
# 
# IMPORTING OTHER FILES
import Import_Data_To_DB as import_data
import Create_Table_And_Import_Data_From_EDGAR as create_Table_and_Import
#
# IMPORTS FOR CHECKING IF DB IS UP TO DATE
import datetime as dt 
#
# IMPORTS FOR EDGAR
from sec_api import QueryApi
import simplejson as json
# 
# 
# IMPORTS FOR SQL DB CONNECTION
import pymysql,os,requests,operator
#
#
# IMPORTS FOR LSTM
# Import the libraries
# Warnings
import warnings
warnings.filterwarnings('ignore')
## math library for mathematical function
import math
## labeled data view in dataframe
import pandas as pd
## data reader od panda is used fetch the data from web
import pandas_datareader as web
## numpy is used to create multi dimensional array
import numpy as np
## tensorflow is uded to create DL model and wrapping the other libraries
import tensorflow as tf
## sklearn is providing ultility functions for standerdizing or scaling data
from sklearn.preprocessing import MinMaxScaler
## keras is a neural network library
from keras.layers import LSTM
from keras.layers import Dense
from keras.models import Sequential

import csv

# CHANGE FIELDS TO YOUR OWN PERSONAL FIELDS
# db = pymysql.connect(
#   host = 'your database hosting site',
#   user = 'your username',
#   password = 'your password',
#   db = 'Name of the database you are connecting to'
# )
# c = db.cursor()
host='your database hosting site'
user= 'your username'
password= 'your password'
db= 'Name of the database you are connecting to'


#THIS WAS OUR DATABASE INFORMATION
host='hedge-fund-13f-filings.cuqh3juyttmr.us-east-1.rds.amazonaws.com',
user='admin',
password='12345678',
db= 'HF_13f_filings'

# OUR WORKING DB
db = pymysql.connect(
  host=host,
  user=user, 
  password=password,
  db=db
)
c = db.cursor()

# This will create the database table, 
# and then import all holdings from the 13F Filing Data from each fund 
# into the table
Your_Table_Name = create_Table_and_Import.run_create_and_import()

#Find the date of the last available filing.
#@param date is the date on which the code is being run
def quarter(date):
    if date.month == 1:
        year = date.year - 1
        return str(year) + '-09-30'

    elif date.month == 2:
        year = date.year - 1
        if date.day < 16:
          return str(year) + '-09-30'
        return str(year) + '-12-31'

    elif date.month == 3:
        year = date.year - 1
        return str(year) + '-12-31'

    elif date.month == 4:
      year = date.year - 1
      return str(year) + '-12-31'
    
    elif date.month == 5:
      year = date.year - 1
      if date.day < 16:
        return str(year) + '-12-31'
      return str(date.year) + '-03-31'
    
    elif date.month == 6:
      return str(date.year) + '-03-31'
    
    elif date.month == 7:
      return str(date.year) + '-03-31'
    
    elif date.month == 8:
      if date.day < 16:
        return str(date.year) + '-03-31'
      return str(date.year) + '-06-30'
    
    elif date.month == 9:
      return str(date.year) + '-06-30'
    
    elif date.month == 10:
      return str(date.year) + '-06-30'
    
    elif date.month == 11:
      if date.day < 16:
        return str(date.year) + '-06-30'
      return str(date.year) + '-09-30'
    
    elif date.month == 12:
      return str(date.year) + '-09-30'
    
last_quarter = quarter(dt.datetime.now())
two_ago = quarter(dt.datetime.now()-dt.timedelta(90))

#Check if database contains the most updated filings
#If not, add the newest data to the database
def check_if_db_is_updated():
  sql = '''
  SELECT * FROM %s.%s
  order by filingDate desc
  limit 1
  ''' % (db, Your_Table_Name)
  c.execute(sql)
  data=c.fetchall()
  most_recent_date = []    
  if(quarter(dt.datetime.now()) != data[0][0]):
      import_data.run_import(1)
      


create_temp_table = '''
Create temporary table sumValues
select sum(valueInDollars) as valSum,cik,cusip,filingDate,nameOfIssuer
from %s
where filingDate = "%s"
group by filingDate, cik, cusip;
''' % (Your_Table_Name, last_quarter)

create_second_temp_table = '''
Create temporary table sumValues2
select sum(valueInDollars) as valSum,cik,cusip,filingDate,nameOfIssuer
from %s
where filingDate in ("%s")
group by filingDate, cik, cusip;
''' % (Your_Table_Name, two_ago)

get_top_25_plus_turnover = '''
SELECT valSum,cik,cusip,nameOfIssuer,filingDate,name,rnk,totals
FROM (
    SELECT s.valSum,s.cik,s.cusip,s.nameOfIssuer,s.filingDate,f.name, v.filingDate as vfilingDate, v.CIK as vCIK, v.valSum as vValSum, (s.valSum - ifnull(v.Valsum,0)) as totals , RANK() OVER  (PARTITION BY s.CIK, s.filingDate ORDER BY s.valSum desc,s.nameOfIssuer) AS rnk
    FROM sumValues as s
    LEFT JOIN sumValues2 as v on (s.CIK = v.CIK and s.cusip=v.cusip and v.filingDate = "%s")
    LEFT JOIN HF_Data as f on (s.CIK = f.CIK)
    order by s.cik, rnk
) AS x
WHERE x.rnk <= 25;
''' % two_ago

drop_temp_table = "drop temporary table sumValues;"

c.execute(create_temp_table)
c.execute(create_second_temp_table)
c.execute(get_top_25_plus_turnover)
data = c.fetchall()
c.execute(drop_temp_table)
json_stocks_string = json.dumps(data)
json_stocks = (json.loads(json_stocks_string))


fund_dict = {}
stock_dict = {}
best_stocks = []

# Assign a score to each stock based on its placement in each fund's top 25
for i in json_stocks:
    i_cik = i[1]
    i_rnk = i[6]
    fund_dict[i_cik] = i_rnk
keys = list(fund_dict)
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
    stock_dict[i_cusip] += new_rank
stocks = list(stock_dict)
for i in range(len(stock_dict)):
    stock_dict[stocks[i]] /= 27
stock_dict = dict(sorted(stock_dict.items(), key=operator.itemgetter(1),reverse=True))
stocks = list(stock_dict)
for i in range(1,2):
    best_stocks.append(stocks[i])

return_list = []

def validate_nine_chars(cusip):
     if(cusip == "46090"):
         return "46090E103"
     zero = 0
     while(len(cusip) < 9):
         cusip = str(zero) + cusip
     return cusip

# this is for transforming the CUSIP into a stock ticker.
for i in range(len(best_stocks)):
    cusip = validate_nine_chars(best_stocks[i])   
    urlBeg = 'https://finnhub.io/api/v1/search?q='
    urlEnd = '&token=c3rnfbaad3i88nmm0ai0'
    fullUrl = str(urlBeg)+str(cusip)+str(urlEnd)
    r = requests.get(fullUrl)
    f = r.json()
    temp = f.get('result')
    temp2 = temp[0].get('symbol')
    return_list.append(temp2)


# Runs the LSTM model on a stock ticker, using training data since January 1, 2018
# @param company is the stock ticker of the company being predicted
# @return the average percent error of actual vs. predicted results.
# percent error is given by 100 * (actual - predicted) / actual
def predict(company):
    start = dt.datetime(2018,1,1)
    end = dt.datetime.now()
    data_frame = web.DataReader(company, 'yahoo', start, end)
    d = quarter(end)

    scaling_data_frame = data_frame.filter(['Open','High','Low','Close','Adj Close','Volume'])
    ## Scaling the features
    scaler = MinMaxScaler(feature_range=(0,1))
    ## Transform the data into
    scaled_Data = scaler.fit_transform(scaling_data_frame)
    ## Display the scaled features into dataframe
    scaled_data_frame = pd.DataFrame(data=scaled_Data, columns=['Open','High','Low','Close','Adj Close','Volume'] )

    ## Create a seperate dataframe with only colse column
    stock_close_data = data_frame.filter(['Close'])

    ## Convert created dataframe into numpy array
    stock_close_dataset = stock_close_data.values

    df1 = data_frame['2000-01-01':d]
    trainingDataLength = len(df1)

    ## Scaling the data its come under preprocessing stage
    ## Create feature range into 0,1
    scaler = MinMaxScaler(feature_range=(0,1))

    ## Transform the data into
    scaledData = scaler.fit_transform(stock_close_dataset)

    ## Create a new dataset which contain scaled value
    StockTrainData = scaledData[0:trainingDataLength , :]

    ## Spliting the dataset into two parts such as Xtrain and Ytrain datasets
    Xtrain = []
    Ytrain = []

    for i in range(60, len(StockTrainData)):
      Xtrain.append(StockTrainData[i-60:i, 0])
      Ytrain.append(StockTrainData[i, 0])

    ## Convert Xtrain data, Ytrain data into numpy array
    Xtrain = np.array(Xtrain)
    Ytrain = np.array(Ytrain)
    
    ## Reshape the Xtrain data (number of column and number of row)
    Xtrain = np.reshape(Xtrain, (Xtrain.shape[0], Xtrain.shape[1], 1))

    ## Develop LSTM model
    model = Sequential()

    ## Assign neurons as 50
    neurons = 50

    ## First LSTM layer
    model.add(LSTM(neurons, return_sequences=True, input_shape= (Xtrain.shape[1], 1))) 

    ## Second LSTM layer, no more layer for lstm so return_sequence is false
    model.add(LSTM(neurons, return_sequences= False)) 

    ## Adding Dense layer which always have 25 neurons by default
    model.add(Dense(25)) 
    model.add(Dense(1))

    ##Compile  model
    ## mse= mean squared error
    model.compile(optimizer='adam', loss='mse')

    ## Fiting model with given training dataset
    history_data = model.fit(Xtrain, Ytrain, batch_size=50, epochs=50, verbose=2, validation_split=0.2)

    ##Create testing dataset, new array which contains scaled value from 2275 out of 2843
    testingData = scaledData[trainingDataLength - 60: , :]

    ## Create dataset Xtest and Ytest
    Xtest = []
    Ytest = stock_close_dataset[trainingDataLength:, :]
    for i in range(60, len(testingData)):
        Xtest.append(testingData[i-60:i, 0])

    ## Convert data into numpy array
    Xtest = np.array(Xtest)

    ## Reshape data from 2 Dimensional to 3 Dimensional
    Xtest = np.reshape(Xtest, (Xtest.shape[0], Xtest.shape[1], 1 ))

    ## Get predicted stock price value
    ## Unscaling the predicted value
    predictions = model.predict(Xtest)
    predictions = scaler.inverse_transform(predictions)

    ## Ploting data to graph train and validation
    training = stock_close_data[:trainingDataLength]
    validation = stock_close_data[trainingDataLength:]
    validation['Predictions'] = predictions

    error = 100*np.mean(Ytest-predictions)/len(Ytest)
    return round(error, 3)

results = []
for s in return_list:    
    results.append({s, predict(s)})
## THIS SECTION HERE ADDS THE DATA TO AN EXCEL SHEET AND CREATES IT IN THE SAME FOLDER

# TOP 25 STOCKS OF EACH FUND TO A NEW SHEET IN THE EXCEL FILE
df = pd.DataFrame(json_stocks)
writer = pd.ExcelWriter('Stock_Analysis_Results.xlsx', engine='xlsxwriter')
df = df.rename(columns = {0:"current Value (In Dollars)",1:"CIK", 2:"CUSIP", 3:"StockName", 4:"FilingDate", 5:"FundName", 6:"Ranked(By Total Value)",7:"Share Change Since Last Quarter"})
df.to_excel(writer, sheet_name='TOP_25_STOCKS_OF_EACH_FUND')
# TOP 25 STOCKS AVERAGED OVER ALL FUNDS 
# PLUS PREDICTION ERROR AND SHARE PRICE DIFFERENCE BETWEEN MOST RECENT QUARTER & ITS PREVIOUS ONE
list_results = []
for stock_pred in results:
    temp_list = []  
    stock_pred = list(stock_pred)
    stock_pred.sort(key = lambda item: ([str,np.float64].index(type(item)), item))
    temp_list.append(stock_pred[0])
    temp_list.append(stock_pred[1])
    start = quarter(dt.datetime.now())
    end = dt.datetime.now()
    company = stock_pred[0]
    data_frame = web.DataReader(company, 'yahoo', start,end)
    EOQ = data_frame['Close'].values[0]
    current = data_frame['Close'].values[len(data_frame)-1]
    temp_list.append(EOQ.round(decimals=2))
    temp_list.append(current.round(decimals=2))            
    diff_dol = current - EOQ
    diff_per = current/EOQ * 100
    temp_list.append(diff_dol.round(decimals=2))
    temp_list.append(diff_per.round(decimals=2))        
    list_results.append(temp_list)


df2 = pd.DataFrame(list_results)
df2 = df2.rename(columns = {0:"Stock Ticker", 1:"Prediction Error", 2:"Closing Share Price on Date of Last Filing", 3: "Latest Share Price for Today", 4:"Change in Share Price($)", 5:"Change in Share Price(%)"})
df2.to_excel(writer, sheet_name = 'Top25AvgOverAllFunds')
writer.save()
c.close()