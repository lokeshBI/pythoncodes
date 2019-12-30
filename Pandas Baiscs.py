# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:17:52 2019

@author: LOKESH
"""

"""   Pandas Baiscs   """

import pandas as pd
import numpy as np

# how to get a dataframe from file

df = pd.read_csv('weather_data.csv')

# basic info about dataframe 

df.shape

df.head()

df.tail()

df.columns

df.index

df.describe()

df.dtypes

type(df.windspeed)

type(df.windspeed[0])

# getting only specific datatype columns | data

df.select_dtypes(include = np.int64)

df.select_dtypes(include = np.int64).columns 

df.select_dtypes(include = np.object).columns
 
# type casting of dataframe 

df.temperature = df.temperature.astype(np.float64)

type(df.temperature[0])

# creating new columns to existing dataframe 

df['event Status'] = np.select([df.event == 'Rain', df.event == 'Sunny'],['bad day', 'hot day'], default = 'no day')

df


df['event status2'] = df.windspeed.apply(lambda x: 'normal wind' if x <= 4 else 'medium wind')
df
                                
df['event status3'] = df.windspeed.apply(lambda x: 'normal wind' if x <= 4 else 'medium wind' if x <=6 else 'hot wind')
df

# rename the existing columns 

df.rename(columns = {'event Status': 'status1', 'event status2': 'status2'}, inplace = True)
df.columns

# dropping columns from a dataframe

df.drop(columns = ['status1', 'status2'], axis = 1)

# slicing a dataframe | filtering  

df[1:5]

df[1:5][['temperature','windspeed']]

df[1:5][:]

df[df.temperature >24][:]

df[(df.temperature >24) & (df.windspeed > 4)][:]

df[(df.temperature >24) & (df.windspeed > 4)][['temperature','windspeed']]

df[df.windspeed.isin(list(range(6)))][:]

df[df.windspeed.between(0,4)][:]

# .loc method of slicing

df.set_index('event',inplace = True)
df

df.loc['Rain'][['temperature','status2']]


df.reset_index('event', inplace = True)
df

# .iloc method of slicing

df.iloc[0:4,2:]

df.iloc[:, 4:]

# sorting a dataframe 

df.sort_values(by = ['temperature'])

df.sort_values(by = ['temperature'], ascending = False)

# group by operations on dataframe 

# police dataset

df = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2018-tutorial/master/police.csv")
df.head()

df.columns 

df.dtypes

len(df)

df.count()

df.select_dtypes(include = np.object).columns

# getting unique values and counts

df.search_conducted.unique()
df.search_conducted.nunique()

df.violation.count() # total counts

df.violation.value_counts() # individual counts

df.groupby('violation').size().sort_values(ascending = False) # individual counts

# for male and female violation counts

df[df.driver_gender == 'M']['violation'].value_counts()

df[df.driver_gender == 'F']['violation'].value_counts()


df.groupby('driver_gender')['violation'].value_counts()

# mean of driver gender search conducted

df.groupby('driver_gender')['search_conducted'].mean()

# sum of driver gender search conducted

df.groupby('driver_gender')['search_conducted'].sum()


df.groupby(['violation','driver_gender']).search_conducted.count()

df.groupby(['violation','driver_gender']).search_conducted.value_counts()

# get the average age of driver_gender from police dataset

df.groupby('driver_gender').driver_age.mean()

# get male and female for driver race

df.groupby('driver_race').driver_gender.value_counts()

# crosstab

pd.crosstab(df.driver_race, df.driver_gender)

pd.crosstab(df.driver_race, df.driver_gender, margins = True)

pd.crosstab(df.driver_race, [df.driver_gender, df.search_conducted], margins = True)

pd.crosstab([df.driver_gender, df.search_conducted],df.driver_race, margins = True)


# handling null values 

dff = pd.DataFrame([range(3), [0, np.NaN, 0], [0, 0, np.NaN],[np.NaN, np.NaN, np.NaN], range(3), range(3)])
dff


dff.rename({0: 'first',1: 'second',2 : 'third'},axis = 1, inplace = True)
dff

# column level
dff.isnull().sum()

# row level
dff.isnull().sum(axis= 1)

# drop all NA records
dff.dropna()

# get data with at leaset one NA 
pd.isnull(dff)

pd.isnull(dff).any(axis= 1)

dff[pd.isnull(dff).any(axis= 1)]

# get only NA reocrds

# create a new column
dff['only null records'] = dff.isnull().sum(axis= 1) 

dff

dff.columns

# get all NA records
dff[dff['only null records']== len(dff.columns)-1 ]
dff


# imputation methods 

dff_new = dff.replace({'third': np.NAN}, np.mean(dff.third))
dff_new


dff_new.second = dff_new.second.fillna( np.mean(dff.second))

dff_new

dff_new = dff_new.replace({'first': np.NAN}, 0)
dff_new

dff_new

