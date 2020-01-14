# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:24:04 2020

@author: LOKESH
"""

##################################  OOPS concepts in python

## class

class Parrot:
    
    # class attributes
    
    # instance attributes
    
    # instance methods
    # A method is defining a fun in the body of class
    pass


obj1 = Parrot()

obj1

## defining a class

class Parrot:
     # class attributes
     species = 'Bird'
     
     # instance attributes
     def __init__(self, name, color,age):
         self.name = name
         self.color = color
         self.age = age


# creating initiate the class
         
p1 = Parrot('kuku','black',5)
p2 = Parrot('pek', 'blue',6)         


# accessing class attributes
p1.__class__.species
p2.__class__.species
# accessing instance attributes

p1.name
p1.color
p1.age

p2.name
p2.color
p2.age

########################################## methods


class Parrot:
     # class attributes
     species = 'Bird'
     
     # instance attributes
     def __init__(self, name, color,age):
         self.name = name
         self.color = color
         self.age = age
 
     # method attributes / instance methods
     def sing(self):
         print('{} gonna sing'.format(self.name))
         
     def dance(self):
         print('this {} and age of {} can dance well'.format(self.color,self.age))
         
     def fly(self, available):
         print('{} with {} color having age of {} available in {}'.format(self.name,self.color,self.age,available))



p1 = Parrot('kuku','black',4)

# accessing class attributes

p1.__class__.species


# accessing instance attributes
p1.name
p1.color
p1.age

# accesssing methods

p1.sing()

p1.dance()

p1.fly('india')


########################################## inheritance


class Parrot:
     # class attributes
     species = 'Bird'
     
     # instance attributes
     def __init__(self, name, color,age):
         self.name = name
         self.color = color
         self.age = age
 
     # method attributes / instance methods
     def sing(self):
         print('{} gonna sing'.format(self.name))
         
     def dance(self):
         print('this {} and age of {} can dance well'.format(self.color,self.age))
         
     def fly(self, available):
         print('{} with {} color having age of {} available in {}'.format(self.name,self.color,self.age,available))



class Parrotkid(Parrot):
    # instance attribiutes
    def __init__(self,name,color,age):
        # use super() to call parent class
        super().__init__( name, color, age)
        
        
     # methods   
    def dance(self):
        return '{} dances so so well'.format(self.name)
    
    def mimik(self,describe):
        return '{} birds are mimiks so so {}'.format(self.name,describe)


## now lets access parent class using child class

p3 = Parrotkid('pegion','white',5)

p3.name

p1.name 

## now access methods

p3.dance() # defining same functions child overides
p3.sing()

p3.fly('india')

p3.mimik('lovely')


######################### example


class Parent:
    
    def __init__(self,fname,lname,profession):
        self.fname = fname
        self.lname = lname
        self.profession = profession
        
    def profession1(self, year):
        return 'this is {}{} he ended his {} profession in the year{}'.format(self.fname,self.lname,self.profession,year)
    
    def profession2(self, year):
        return 'this is {}{} he ended his {} profession in the year{}'.format(self.fname,self.lname,self.profession,year)
    

class Student(Parent):
    
    def __init__(self,fname,lname,profession,whatstudy):
        super().__init__(fname,lname,profession)
        self.whatstudy = whatstudy
        
    def school(self, studying):
        return '{}{} studying {}'.format(self.fname, self.lname,studying)
    
    def college(self, studying):
        return '{}{} studying {} college'.format(self.fname, self.lname,studying)

## accessing parent class
fir = Parent('fransis','abignale','lawyer')

fir.fname
fir.lname

fir.profession1(2019)
fir.profession2(2020)

## accessing child class
chi = Student('kate','sims','baseball','school')

chi.fname
chi.profession

chi.college('middlton')

chi.school('emma grammer')

# accessing parent class from child class

chi.profession1(2019)

chi.profession2(2020)



########################################### Data Encapsulation
# Using OOP in Python, we can restrict access to methods and variables. 
# This prevent data from direct modification which is called encapsulation. 
# In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()

c.sell()

## try to change the price

c.__maxprice = 100

c.sell()

# try to change maxprice using function

c.setMaxPrice(100)

c.sell()

#################################################### polymorphism


class tiger:
     # class attributes
     species = 'animal'
     
     # instance attributes
     def __init__(self, name, color,age):
         self.name = name
         self.color = color
         self.age = age
 
     # method attributes / instance methods
     def sing(self):
         print('{} gonna sing'.format(self.name))
         
     def dance(self):
         print('this {} and age of {} can dance well'.format(self.color,self.age))
         
     def fly(self, available):
         print('{} with {} color having age of {} available in {}'.format(self.name,self.color,self.age,available))



class Parrot:
     # class attributes
     species = 'Bird'
     
     # instance attributes
     def __init__(self, name, color,age):
         self.name = name
         self.color = color
         self.age = age
 
     # method attributes / instance methods
     def sing(self):
         print('{} gonna sing'.format(self.name))
         
     def dance(self):
         print('this {} and age of {} can dance well'.format(self.color,self.age))
         
     def fly(self, available):
         print('{} with {} color having age of {} available in {}'.format(self.name,self.color,self.age,available))


f1 = tiger('titi','strips',12)
f2 = Parrot('pika','green',6)


## ploymorph function


def polymorph_fun(x):
    x.sing()
    x.dance()
    x.fly('Goa')


polymorph_fun(f1)

polymorph_fun(f2)





































































