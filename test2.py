'''Q1 write a python function that takes two lists and returns
True if they have atleast one common member'''

def common_member(list1,list2):
   common=[a for a in list1  if a in list2 ]
   return True
common_member([1,2,1],[2,3,4])

''' Q2 Use list comprehension to construct a new list but add
6 to each item'''
list1=[1,2,3,4,5]
lst=[x ++6 for x in list1]
print(lst)

'''Q3 write a python program to reverse a string'''
string1="Sayali"
s=string1[::-1]
print(s)


''' Q4 write a python program to iterate over dictionaries
using for loop'''
dict1={'X':10,'Y':20,'Z':30}
for dict_keys,dict_values in dict1.items():
    print(dict_keys,':',dict_values)
   
'''Q5 using dict comprehension and a conditional argument 
create a dictionary from the current dictionary 
where only the key value pairs with value above 2000
are taken to the new dictionary
'''


'''Q6 open the file data.txt using file operations'''
with open('data.txt') as file_object:
    c=file_object.read()
    print(c)
    
'''Q7 write a python program to construct an infinite iterator that returns
evenly spaced values starting with a 
specified number and step'''


    
'''Q8 write a python program to filter a list of integers using
lambda function'''
list1=[1,2,3,4,5,6,7,8,9,10]
even=lambda x:x%2==0 
filter_list=list(filter(even,list1))
print("Even list")
print(filter_list)
odd=lambda x:x%2!=0
filter_list=list(filter(odd,list1))
print('Odd list')
print(filter_list)


'''Q9 write a pandas program to create the given data frame'''
import pandas as pd
df={'name':['Anna','Dinu','Ramu','Ganu','Emily','Mahesh','Jayesh','Venkat','Ajay','Dhanesh'],
    'score':[12.5,9,16.5,'np.nan',9,20,14.5,'np.nan',8,19],
    'attempts':[1,3,2,3,2,3,1,1,2,1],
    'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes'],}
labels=['a','b','c','d','e','f','g','h','i','j']
df1=pd.DataFrame(df,index=labels)
df1
'''Q10 write a python program to plot two or more lines and set the line marker
'''
import matplotlib.pyplot as plt
import numpy as np
x=range(1,5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()



