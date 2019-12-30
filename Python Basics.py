# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:35:42 2019

@author: LOKESH
"""

"""  Python Fundamentals """

# printing options
# .format method

print("hey there! %s. This is Python" %'welcome')
print("hello world! this is %s and %s" %('cat','dog'))
print("hello world! this is {} {} with long {}.".format('blue','bear','tail'))
print("hello world! this is {} & {} with long {}.".format(1,2,3))
print("hello world! this is {1} & {0} with long {2}.".format(1.5,2.5,3)) 
print("hello world! this is %s and %r" %('cat','dog'))

## lists
## lists are mutable 

list1 = [10,20,30,'cat',True]
print(list1)

list2 = [50,60,70,'dog']
print(list2)

## concatenate lists
print(list1 + list2)    ## extend and concatenation will do the same

## appending a list
list3 = list1.append(list2)
print(list3)            ## don't assign a list to another list while appending

print(list1)            ## this is called appending and it's appending a list at last

list3 = [11,12,13,15]
list2.extend(list3)     ## extending is different than appending, extending always do add up as elements but not as list
print(list2)

## lists are mutable objects so lets do slicing and update the list

print(list2[1:])
print(list2[:3])
print(list2[1:5:2])
print(list2[::-1])      ## reversing
print(list2[:-1:], "\n", "\n mutable: ")

print(list2)
list2[4] = 'cat'  ## updating a list
print(list2)

## update each even element in the list with number 2
list4 = [1,2,3,4,5,6,7,8,10]
len(list4)
list4_uu = [  i*2 for i in range(1,len(list4),2) ]  ## list comprehension
print(list4_uu)

## nested lists
list_nested = [[1,2,3],['apple',5,6],[50,15],{'a':[1,2,3],'b':[14,20]}]
print(list_nested)

## slicing and dicing a nested list
print("\n",list_nested[0])
print(list_nested[0][0])
print(list_nested[1][2])
print(list_nested[3])
print(list_nested[3]['a'][1])


## list methods

a = [10,20,30,40,50]
b = [11,12,13,14,15]
print(a)
print(b)

# append()

a.append(b)
print(a)

# extend()

a.extend(b)
print(a)

# insert()
b.insert(5, 'apple')
b

# remove()
b.remove('apple')
b

# pop()
a.pop(2)
a

a.pop()
a

# count()
a
a.count(10)

# clear()
a.clear()
a

# index()
b
b.index(13)

# sorting
b.sort()
b
b.sort(reverse = True)
b

b.sort()

# reverse()

b.reverse()
b

# dictionaries

di = {'a':[1,2,3],'b':['tom','peter',20],'c':[11,12,13],'d':{'ds':[9,8,7],'ab':['blue','green']}}
di

di.keys()
di.values()

# slicing and dicing
di['a'][2]
di['d']['ds'][2]
di['d']['ab'][0]

# example
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}

print('Dict keys:', list(Dict.keys()),"\n")
print('Boys keys:',list(Boys.keys()),"\n")

for i in list(Dict.keys()):
    if i in list(Boys.keys()):
        print(i, ': exist')
    else:
        print(i, ': Not exists')

# len()
len(Dict)        

# useful operators
list(range(0,10))

# range() with step size
list(range(0,10,2)) 

# zip 
list1 = [21,22,23,24]
list2 = [25,26,27,28]
list(zip(list1,list2))

# zip always takes equi length lists
list1 = [21,22,23,24,25]
list2 = [25,26,27,28]
list(zip(list1,list2))


for i, j in list(zip(list1, list2)):
    print('first number is {} and second is {}'.format(i,j))


# in operator
20 in [10,20,30,4]    

# not in
20 not in [10,20,50,5]


# list comprehensions

p = [i**2 for i in list(range(0,10))]
p

q = [i**2 for i in list(range(0,10)) if (i**2)%2 == 0]
q

w = [ i*3 for i in (i*2 for i in list(range(0,5)))]
w

e = ['even' if i % 2 == 0 else 'odd'  for i in list(range(0,10))]
e

e = ['even' if i % 2 == 0 else 'odd'  for i in list(range(0,10))]
e

# map() function

def num1(x):
    return x**2

a = list(range(0,10))
a

list(map(num1, a))


## map & lambda
a = list(range(0,10))
a

list(map(lambda x : x**2, a))

## counter()

from collections import Counter

cdd = [12,12,15,15,15,15,14,1,18,18] 
Counter(cdd)

## split()

df = 'Hey there this is spiderman wanna mess with me!'
df.split()

Counter(df.split())






