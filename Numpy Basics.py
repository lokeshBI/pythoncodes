# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 11:21:16 2019

@author: LOKESH
"""

"""    Numpy Basics """

import numpy as np

# arrays
a1 = [10,20,30,40]
a1
a2 = np.array(a1)
a2

a2.ndim
a2.shape
a2.dtype


arr1 = [[1,2,3],[4,5,6]]
arr2 = np.array(arr1)
arr2 

arr2.ndim
arr2.shape
arr2.dtype

arr3 = [[1,2,3],[4,5,6],[7,8,9]]
arr4 = np.array(arr3)
arr4

arr4.ndim
arr4.shape
arr4.dtype

#  array of zero's

a1 = np.zeros(10)
a1

a1.ndim
a1.shape
a1.dtype

a2 = np.zeros((2,3))
a2

a2.ndim
a2.shape
a2.dtype


a3 = np.zeros((2,3,4))
a3

a3.ndim
a3.shape
a3.dtype

# array of ones


a1 = np.ones(10)
a1

a1.ndim
a1.shape
a1.dtype

a2 = np.ones((2,3))
a2

a2.ndim
a2.shape
a2.dtype


a3 = np.ones((2,3,4))
a3

a3.ndim
a3.shape
a3.dtype


# empty array

a4 = np.empty(10)
a4

a5 = np.empty((2,3))
a5

a6 = np.empty((2,3,2))
a6

# full()

a7 = np.full((2,3,2), 3.5,dtype = np.int)
a7


a7 = np.full((2,3,2), 3.5)
a7

# eye()

a9 = np.eye(2,2)
a9


a9 = np.eye(2)
a9


a9 = np.eye(3)
a9


# arange()

a1 = np.arange(0,10)
a1


a1 = np.arange(0,10,2)
a1

# linspace()

a1 = np.linspace(0,10,5)
a1


a1 = np.linspace(0,10,10)
a1


# randint
# randint(lowest number, highest number, size)

x1 = np.random.randint(10, size = 10)
x1

x2 = np.random.randint(0,10, size = (2,2))
x2

x3 = np.random.randint(1,10, size = (2,3,2))
x3


x4 = np.random.randint(1,10, size = (2,3,4))
x4

# slicing a 3D array

a1 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
a1

a1.ndim

# pick 8
a1[0,2,1]

# pick 14
a1[1,1,1]

# pick 10
a1[1,0,0]

# pick 6
a1[0,1,2]

# pick a sebset of array like [14,15,17,18]

a1[1,1:,1:]


# arrange() and reshape()
# serial number array generators 

a = np.reshape(np.array(np.arange(0,6)), newshape = (2,3))
a

b = np.reshape(np.array(np.arange(0,24)), newshape = (2,3,4))
b

f = np.reshape(np.array(np.arange(0,12)), newshape = (2,3,2))
f

# random number generator arrays

u = np.random.randint(1,20, size = (2,3,4))
u


k = np.reshape(np.array(np.random.randn(12)), newshape = (2,3,2))
k

# unique()
np.unique(u)

# type casting of an array

u = np.random.randint(1,20, size = (2,3,4))
u

y = u.astype(np.float)
y

# randn()
d = np.random.randn(10)
d

e = np.random.randn(2,3)
e

e = np.random.randn(2,3,4)
e


# create 3D array with serial numbers

np.reshape(np.array(np.arange(24)), newshape= (2,3,4))

np.arange(24).reshape((2,3,4))

# create 3D array with random numbers between 1,10

np.random.randint(1,10, size = (2,3,4))

# create 3D array with random numbers

np.random.randn(2,3,4)



# create normal distribution of elements

a = np.random.normal(size = (4,4))
a

import matplotlib.pyplot as plt

plt.hist(a)
plt.show()


# sorting an array
a = np.random.normal(size = (4,4))
a

np.sort(a)
