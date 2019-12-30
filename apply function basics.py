# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 12:33:00 2019

@author: Lokesh
"""

# Difference between apply(), applymap() and map() functions in python.

import pandas as pd
import numpy as np

df = pd.read_csv('http://bit.ly/kaggletrain')

df.columns


# map()
# map() only works for dataframe series.

df['sex code'] = df.Sex.map({'female': 0, 'male': 1 })

df.loc[:, ['Sex', 'sex code']].head()

df.Sex.map(len).head()


# apply() function can be performed by both series level and dataframe levelk as well.

# apply() function as a series method

# method1
def encoderfun(x):
    if x == 'female':
        return 0
    else:
        return 1

df['sex code1'] = df.Sex.apply(encoderfun)

df.loc[:, ['Sex', 'sex code1']].head()

#method2

lambda x : 0 if x == 'female'  else 1


df['sex code2'] = df.Sex.apply(lambda x : 0 if x == 'female'  else 1)

df.loc[:, ['Sex', 'sex code2']].head()



# find length of the name 

df['name length'] = df.Name.apply(len)

df.loc[:, ['Name','name length']].head()

# round off the fare 

df['fare ceiling'] = df.Fare.apply(np.ceil)

df.loc[:, ['Fare','fare ceiling']].head()

# square the fare ceiling using lambda function

df['squared fare'] = df['fare ceiling'].apply(lambda x : x ** 2)

df.loc[:, ['fare ceiling','squared fare']].head() 


# apply() function as a DataFrame method.


dff = pd.read_csv('http://bit.ly/drinksbycountry')

dff.columns

dff.select_dtypes(include = np.int64).head()

# find max value on each int column 

dff.select_dtypes(include = np.int64).head().apply(max)

dff.select_dtypes(include = np.int64).head().apply(min)

dff.select_dtypes(include = np.int64).head().apply(sum)

dff.select_dtypes(include = np.int64).head().apply(np.mean)


# applymap()
# applymap() Function performs the specified operation for all the elements in the dataframe.

dff['double_beer_servings'] = dff.beer_servings.applymap(lambda x : x**2) ## it won't work


dff.select_dtypes(include = np.int64).head().applymap(lambda x : x ** 2)










