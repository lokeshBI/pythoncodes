# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:59:08 2020

@author: LOKESH
"""

################# Forecasting cab bookings

import pandas as pd
import numpy as np
from pandas import datetime


def parser(x):
    return pd.to_datetime(x).strftime('%Y-%m-%d')


wdata = pd.read_csv('wd_data_24.csv',encoding = 'utf-8', usecols = ['Date'], parse_dates = ['Date'],date_parser = parser)

type(wdata)

wdata.head(50)

wdata.columns

type(wdata.Date[0])

wdata = wdata.Date.dt.date

df = pd.DataFrame(wdata)

type(df.Date[0])

df.columns


df.isna().sum()

value_counts = df['Date'].value_counts()

df = value_counts.rename_axis('Dates').reset_index(name='Bookings')

df.columns

dff = df.sort_values(by = 'Dates')

# now I have a dff dataframe with all dates and bookings fixed.
# we delted 2016 record cause we have only one data point on that date.

dff = dff.iloc[1:, :]

dfp = dff.set_index('Dates')


## plotting the data

import matplotlib.pyplot as plt

dfp.plot()

## check for acf plot for stationary or not.

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(dfp)


## check for stationary
## take mean , variance between different time periods and check



# we are shifting one for stationary.
# in ARIMA model it's called d = diffrenciation
df_onelag = dfp.diff(periods = 1)

df_onelag = df_onelag.iloc[1:, :]

df_onelag.plot()

##


X = dfp.values
len(X)

train = X[0:200]
test = X[199:280]

len(train)
len(test)

# try to build very basic model

from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

model_ar = AR(train)
model_ar_fit = model_ar.fit()

predictions = model_ar_fit.predict(start = 200, end = 280)

plt.plot(test)
plt.plot(predictions, color = 'red')

dfp.plot()

# try to build ARIMA model
# Auto Regressive Integrated Moving Average

from statsmodels.tsa.arima_model import ARIMA
 
# p, q and d are the parameters 
# p = periods taken for regressive model
# d = integration order --> difference typically 1 or 2
# q = periods in moving average model
arima_model = ARIMA(train, order = (3,1,3))
arima_model_fit = arima_model.fit()
print(arima_model_fit.aic)

predictions_arima = arima_model_fit.forecast(steps = 80)

predictions_arima1 = predictions_arima[0]

plt.plot(test)
plt.plot(predictions_arima1, color = 'red')

## error
mean_squared_error(test, predictions_arima1)



# to find out the best parameters (p,d,q)

import itertools

p=d=q= range(0,5)
pdq = list(itertools.product(p,d,q))
pdq

import warnings
warnings.filterwarnings('ignore')
for param in pdq:
    try:
        arima_model = ARIMA(train, order = param)
        arima_model_fit = arima_model.fit()
        print(param, arima_model_fit.aic)
    except:
        continue

# out of all AIC 924 is the minimum value for the combination (3,1,3)    











