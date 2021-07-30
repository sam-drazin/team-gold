import time
start_time = time.time()
##Import the libraries
# Warnings
import warnings
warnings.filterwarnings('ignore')
## math library for mathematical function
import math
## labeled data view in dataframe
import pandas as pd
#import pandas_datareader as web
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
## it is uded to create plotting area
# import matplotlib.pyplot as mtlplt
## feature scaling distribution
# from matplotlib import rcParams

import datetime as dt
#from datetime import timedelta

#Hedge Funds need only file for the end of the quarter 45 days after the quarter ends.
#Return the date of the newest 13F filings available based on the date passed as a parameter.
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

#Generate a projection from end of quarter until present using LSTM
#return the % error between the predicted and actual results
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


    # ## Ploting data to graph train and validation
    training = stock_close_data[:trainingDataLength]
    validation = stock_close_data[trainingDataLength:]
    validation['Predictions'] = predictions

    error = 100*np.mean(Ytest-predictions)/len(Ytest)
    return error


results = []
for a in ('FB', 'MSFT', 'BABA', 'SPY', 'GOOGL', 'QQQ', 'UBER', 'NFLX', 'IWM', 'DIS'):
    print("Predicting " + a)
    results.append(predict(a))
print(results)
# ## Visualize trainning, validating and predicting values in graph
# mtlplt.figure(figsize=(20,10))
# mtlplt.title('2015, 75 Epochs')
# mtlplt.xlabel('Date', fontsize=20)
# mtlplt.ylabel('Close Stock Price $ (USD)', fontsize=20)
# mtlplt.plot(training['Close'])
# mtlplt.plot(validation[['Close', 'Predictions']])
# mtlplt.legend(['Training', 'Validation', 'Predictions'], loc='lower right')
# mtlplt.show()