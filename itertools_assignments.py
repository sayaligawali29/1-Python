# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 03:06:06 2023

@author: user
"""

#write a python program to an iterator from several iterator in sequence 
#and display the type and element of new iterator

#chain() 
#chain is used in deep learning
#list
from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result=chain_fun([1,2,3],['a','b','c'],[4,5,6])
print('type of new iterator:')
print(result)
print("Elements of new iterator:")
for i in result:
    print(i)
#tuple
from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result=chain_fun((1,2,3),('a','b','c'),(4,5,6))
print('type of new iterator:')
print(result)
print("Elements of new iterator:")
for i in result:
    print(i)
    
#write python program that generates the running product
#of elemenys in an iterable
#operator is a module in which mul function is present
from itertools import accumulate
#list
import operator
def run_product(lst):
    return accumulate(lst,operator.mul)
result=run_product([1,2,3,4,5,6,7])
print("Running product of a list:")
for i in result:
    print(i)

#Tuple
from itertools import accumulate
import operator
def run_product(lst):
    return accumulate(lst,operator.mul)
result=run_product((1,2,3,4,5,6,7))
print("Running product of a list:")
for i in result:
    print(i)
    
#write a python program to construct an infinite iterator that
#returns evenly spaced values starting with specified num or step

import itertools as it
start=10
step=1
print("The starting number is ",start,"and step is",step)
my_counter=it.count(start,step)
print("The said function point never ending items")
for i in my_counter:
    print(i)
    
#write python to generate infinite cycle of elements from an iterable

import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result=cycle_data(['A','B','C','D'])
result=cycle_data("Python itertools")
for i in result:
    print(i)
    
#String
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result=cycle_data("Python itertools")
for i in result:
    print(i)
    
#write a python program to make an iterator that drops elements
#from the iterable as soon as an element is a positive number

import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0,nums)
nums=[-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result=drop_while(nums)
print("Drops elements from the iterable when a +ve numbers arises \n",list(result))
