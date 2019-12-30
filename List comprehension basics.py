# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:32:45 2019

@author: Lokesh
"""

# List comprehension models


import numpy as np

list1 = list(range(10))
list1

# get squres

[np.square(i) for i in list1]


# get squres for even numbers

[np.square(i)  for i in list1 if i % 2 == 0]


# show the numbers even or odd

['even' if i % 2 == 0 else 'odd' for i in list1]


# show the numbers with two different conditions

[np.square(i)  if i % 2 == 0 else np.sqrt(i) if i % 3 == 0 else i for i in list1]

# flaten the matrix

matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[np.square(j) for i in matrix for j in i ]


# create a list with all even multiples of 5

[i for i in list(range(101)) if i % 2 == 0 if i % 5 == 0 ]




























