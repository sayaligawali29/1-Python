# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:29:00 2023

@author: user
"""

########GENERATOR##################
# it is another way of creating iterators
#in a simple way where
#it uses the keyword "yeild"
#instead of returning it in a defined function
#generator are implemented using function

gen=(x for x in range(3))
print(gen)
#<generator object <genexpr> at 0x000001D0D3D26330>
#object created
for num in gen:
    print(num)
#Output
#0
#1
#2
################
#next() it is going to show the o/p step by step
gen=(x for x in range(3))
next(gen) ##0
next(gen) ##1

#########################
#Function which return multiple values
def range_even(end):
    for num in range (0,end,2):
        yield num
for num in range_even(6):
    print(num)
#output
#0
#2
#4

#####now instead of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
##0
##2

###Chaining Generator########
#ele* content multiple values

def lengths(itr):
    for ele in itr:
        yield len(ele)
#lengths function is used to calculate length of pass
def hide(itr):
    for ele in itr:
        yield ele* '*'
passwords=["not-good","good'm-pass","00100=100"]
for passwords in hide(lengths(passwords)):
    print(passwords)
##OUTPUT
#********
#***********
#*********

##########Enumerate
##printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
#output
#1 milk
#2 Egg
#3 Bread

#####Same code can be implemented using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
#output
#1 milk
#2 Egg
#3 Bread

