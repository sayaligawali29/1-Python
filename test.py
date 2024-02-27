# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 00:58:18 2023

@author: user
"""
''' q9- write a numpy program to test whether none of the element
of given array are zero'''
import numpy as np
x=np.array([0,1,2,3,4])
print(x)
print(np.all(x))

'''
q1- write a python program to sum all the elements
'''
s=[2,3,4]
sum=0
for x in s:
    sum=sum+x
print(sum)

s=[2,3,4]
print(sum(s))

'''
q2 create an identical list from the first list using list 
comprehension
'''
lst1=[2,4,5,6]
lst=[num ++ 2 for num in lst1]
print(lst)

'''
q3 write a python function to multiply all the numbers in list
'''

def mul_n(items):
    mul=1
    for x in items:
        mul=mul*x
    return mul
print(mul_n([2,3,4]))

'''
q5- first create a range from 100 to 160 with steps of 10 using
dict comprehension
'''

dict={x:x+10  for x in range(100,160)}
dict

'''
write a python program to read an entire file
'''
with open ('programming.txt') as file_object:
    contents=file_object.read()
    print(contents)
    
'''Write a lambda function that takes x as
 parameter and returns x+2.Then assign it to a variable name L

'''
L=lambda x:x+2 
result=L(5)
print(result)

'''write a pandas program to create a dataframe from a 
dictionary and display it'''
import pandas as pd
df={'X':[78,85,96,80,86],
    'Y':[84,94,89,83,86],
    'Z':[86,97,96,72,83]}
df1=pd.DataFrame(df)

    
