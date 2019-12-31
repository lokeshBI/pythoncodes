# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:51:38 2019

@author: LOKESH
"""

import pandas as pd
import numpy as np


# working data sets

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
movies = pd.read_csv('http://bit.ly/imdbratings')
orders = pd.read_csv('http://bit.ly/chiporders', sep='\t')
orders['item_price'] = orders.item_price.str.replace('$', '').astype('float')
titanic = pd.read_csv('http://bit.ly/kaggletrain')

# create an example dataframe

np.random.rand(10,5) # always 2D for a dataframe, here I m giving 10 rows and 5 columns 

pd.DataFrame(np.random.rand(10,5))

np.random.randint(1,10, size = (5,4)) # 5 rows and 2 columns with a random integer between 1 and 10

pd.DataFrame(np.random.randint(1,10, size = (5,4)), columns = list('abcd'))


# rename columns 

drinks.columns 

df = drinks 

df = df.rename({'country': 'county', 'beer_servings': 'beerserves'}, axis = 'columns')

df.columns


# adding prefixes & suffixes for identification of data

drinks.columns

# lets say except country, all other columns are inputs in a drinks data set

df = drinks

df.iloc[:, 1:].add_suffix('_x').columns 

df.iloc[:, 0:1].add_prefix('_Y').columns  # you can use suffix here as well

# reverse the column order of a dataframe

drinks.head()

drinks.iloc[:, ::-1].head()

# select columns by data type 

drinks.dtypes

drinks.select_dtypes(include = np.int64).head()

drinks.select_dtypes(include = np.object).head()

drinks.select_dtypes(include = np.float64).head()

drinks.select_dtypes(include = [np.int64, np.object]).head()

# splitting a data frame into 2 subsets 

movies.columns 

len(movies)

movies1 = movies.sample(frac = 0.75, random_state = 1245)

len(movies1)

movies2 = movies.drop(movies1.index)

len(movies2)

len(movies1)+len(movies2)

movies1.index.sort_values()

movies2.index.sort_values()


# filter a dataframe by largest category

movies.columns 

movies.genre.value_counts()

movies.genre.value_counts().nlargest(3) # here I ma taking N largest

movies.genre.value_counts().nlargest(3).index

movies.iloc[:, 2:5][movies.genre.isin (movies.genre.value_counts().nlargest(3).index)].head(10)


# aggregate by multiple functions

orders.columns 

orders.groupby('order_id').item_price.agg(['sum','count','max']).head(10)


# convert a contineous data into categorical data

titanic.columns

titanic.Age.head()

pd.cut(titanic.Age, bins = [0,18,25,99], labels = ['child','young adult', 'adult']).head(10)


# pandas dataframe profiling 
# for this first you need to install pandas profiling and then it will work. better to try this in jupyter notebook.
# pandas profiler basically gives the complete stats about a dataset which we pass to profile report function.

import pandas_profiling

pandas_profiling.ProfileReport(titanic)














