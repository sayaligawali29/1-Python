# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 04:12:29 2023

@author: user
"""

##write a python script to add a key to a dictionary
##sample dic:{0:10,1:20}
#Expected dic:{0:10,1:20,2:30}
#update() is used to update the dic
d={0:10,1:20}
print(d)
d.update({2:30})
print(d)
#output {0: 10, 1: 20, 2: 30}
###or 
d={0:10,1:20}
print(d)
d[2]=30
print(d)
##output {0: 10, 1: 20, 2: 30}

#######
#write a python script to concatenate the following dic 
#to create new one
#sample dic
#d1={1:10,2:20}
#d2={3:30,4:40}
#d3={5:50,6:60}
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for dic in(d1,d2,d3):d4.update(dic)
print(d4)
###output {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#************************************************
###write a python script to check whether a given key already
#exist or not
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print("Present")
    else:
        print("Not Present")
is_key_present(6)
is_key_present(9)

##########################################
#write a python program to iterate over dictionaries using for loops
d={'x':10,'y':20,'z':30}
for dict_key,dict_value in d.items():
    print(dict_key,':',dict_value)
#output
#x : 10
#y : 20
#z : 30