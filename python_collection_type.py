# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 03:05:55 2023

@author: user
"""

#######Python collection types
#tuple:() a collection of objects that are ordered and immutable
#list:
#dictionary
#set

##tuple
tup1=(1,3,5,6)
print(f"tup1[0]:\t{tup1[0]}")
print("tup1[1]:\t",tup1[1])
print("tup1[2]:\t",tup1[2])
print("tup1[3]:\t",tup1[3])
#output
#tup1[0]:	1
#tup1[1]:	 3
#tup1[2]:	 5
#tup1[3]:	 6

#####tuples can hold different data types
tup2=(1,"Sayali",True,-23.45)
print(tup2)
##output (1, 'Sayali', True, -23.45)

########Iterating over Tuples
tup3=("apple","orange","plum","apple")
for x in tup3:
    print(x)
len(tup3)
#output 
#apple
#orange
#plum
#apple

##########u can count how many times the specified value occurs
tup3=("apple","orange","plum","apple")
#tuples allows duplicate
#count() is used to count the values which is repeated 
tup3.count("apple")
##output 2

############
tup3=("apple","orange","plum","apple")
print(tup3.index("apple"))
print(tup3.index("orange"))


###########
tup3=("apple","orange","plum","apple")
if "orange" in tup3:
    print("orange is in Tuple")
#output orange is in Tuple

######Nested Tuple
tup1=(1,2,3,5)
tup2=("John","Adam","Denise","Phoebe")
tup3=(42,tup1,tup2,5.5)
print(tup3)
# it is not possible to add or remove
#output (42, (1, 2, 3, 5), ('John', 'Adam', 'Denise', 'Phoebe'), 5.5)

######################LIST###########################
#List is mutable and ordered can change or delete element
#heterogeneous types of data
#[] used to defined list

list1=["John","Paul","George","Ringo"]
list2=[1,43.5,True]
root_list=["John",list1,list2,"Denise"]
print(root_list)
###output
##['John', ['John', 'Paul', 'George', 'Ringo'], [1, 43.5, True], 'Denise']

#############Accessing elements from a list
list1=["John","Paul","George","Ringo"]
print(list1[-1])
###output Ringo

#######
list1=["John","Paul","George","Ringo"]
print("list1[1]:",list1[1])
#Paul
print("list1[-1]:",list1[-1])
#Ringo
print("list1[1:3]:",list1[1:3])
#['Paul', 'George']
print("list1[:3]:",list1[:3])
#['John', 'Paul', 'George']
print("list1[1:]:",list1[1:])
#['Paul', 'George', 'Ringo']

########Adding to a list######################3
#append is use to add at the end 
list1=["John","Paul","George","Ringo"]
list1.append("pete")
print(list1)
#['John', 'Paul', 'George', 'Ringo', 'pete']

#extend
#add multiple elements to list or multiple list
list1=["John","Paul","George","Ringo","pete"]
list1.extend(["Ade","Cher"])
print(list1)
#output ['John', 'Paul', 'George', 'Ringo', 'pete', 'Ade', 'Cher']

########insert
list1=["John","Paul","George","Ringo","pete"]
print(list1)
list1.insert(1,"Pam")
print(list1)
#output ['John', 'Pam', 'Paul', 'George', 'Ringo', 'pete']

#######list concatenation
list1=[3,2,1]
list2=[6,5,4]
list3=list1+list2
print(list3)
#output[3, 2, 1, 6, 5, 4]


###assignments
#take 5 numbers in list find min and max 
#take 5 strings in list make it reverse
#take 10 numbers in list write script to search for value e.g 1,1,4
#take 10 numbers insert some duplicate write scrpit to find duplicates
#take vowels in list and non vowels find total numbers of vowels in the list



#assign 1
#minimum and maximum
list1=[1,5,3,7,4]
min(list1)
#min=1
list1=[1,5,3,7,4]
max(list1)
#max=7

#assign 2
list1=["Apple","Ball","Cat","Dog","Mango"]
list1.reverse()
print(list1)
##output ['Mango', 'Dog', 'Cat', 'Ball', 'Apple']
##or
list1=["Apple","Ball","Cat","Dog","Mango"]
rev=list1[::-1]
print(rev)

##assign 3
list1=[11,12,13,14,15,16,17,18,19,20]
print(list1.index(12))
print(list1.index(19))
#####OR
list1=[21,35,47,65,59,72,61,49,96,85]
x=int(input("Enter Number :"))
if x in list1:
    print("Present")
else:
    print("not present")

###assign 4

list4=[32,12,14,45,32,46,37,12,29,46]
num=int(input("Enter number:"))
if list4.count(num)>=2:
    print(num, "is duplicate")
elif list4.count(num)==1:
    print(num, "is not duplicate")
else:
    print(num, "is not present")
    
####assign 5



###########################
#removing from list 
#remove()method is used
#used for web scraping application
another_list=['Gray','Mark','Robbie','Jason','Howard']
print(another_list)
another_list.remove('Robbie')
print(another_list)
#output ['Gray', 'Mark', 'Robbie', 'Jason', 'Howard']

########pop() method 
#it differ from the remove method
#it removes an element from list
#it takes an index which is the index of item to remove from list
#than the object itself
another_list=['Gray','Mark','Robbie','Jason','Howard']
print(another_list)
another_list.pop(3)
print(another_list)
#output ['Gray', 'Mark', 'Robbie', 'Howard']

###################SET#################
#it dont allow duplicate elements
#creating a set
basket={'apple',"orange","apple","pear"}
print(basket)
#output {'orange', 'pear', 'apple'}

####accessing elements from list
for item in basket:
     print(item)
#orange
#pear
#apple

##Adding items to set
set1={"ram","sam","om","sai"}
set1.add("Saai")
print(set1)

###update()
set1={"ram","sam","om","sai"}
set1.update(['a','b'])
print(set1)
#output 
#{'a', 'b', 'ram', 'sai', 'om', 'sam'}

#obtaining the length of set
set1={"ram","sam","om","sai","ram"}
print(len(set1))
#output 4

#obtaining max and min value in a set
set2={1,4,5,7,9}
print(max(set2))
print(min(set2))

####removing an item
set1={"ram","sam","om","sai",}
print(set1)
set1.remove("ram") 
set1.discard("om")
print(set1)

########Set Operation#####
###union is used |
##intersection &
###difference -
s1={"apple","orange","banana"}
s2={"grape","lime","banana"}
print("union:",s1|s2)
print("intersection:",s1&s2)
print("Difference:",s1-s2)

###############################################
###Dictionary
##between a key and a value that is unordered
# changeable (mutable) and indexed

###creating dictionary
capitals={"Maharashtra":"Mumbai","UP":"Lacknow","AP":"Hydrabad"}
print(capitals)
#outpt{'Maharashta': 'Mumbai', 'UP': 'Lacknow', 'AP': 'Hydrabad'}

######Accessing items via keys
print("capitals[Maharashtra:]",capitals['Maharashtra'])
#output capitals[Maharashtra:] Mumbai

###adding a new value
capitals["West_Bengal"]="Gandhinagar"
print(capitals)
#{'Maharashtra': 'Mumbai', 'UP': 'Lacknow', 'AP': 'Hydrabad', 'West_Bengal': 'Gandhinagar'}

###### Changing a Keys Value
capitals["Gujrat"]="Gandhinagar"
print(capitals)

####removing an entry#####
capitals={"Maharashtra":"Mumbai","UP":"Lacknow","AP":"Hydrabad"}
capitals.pop("UP")
print(capitals)
##output {'Maharashtra': 'Mumbai', 'AP': 'Hydrabad'}
capitals={"Maharashtra":"Mumbai","UP":"Lacknow","AP":"Hydrabad"}
capitals.pop("UP")
print(capitals)
del capitals ["AP"]
print(capitals)

####iterating over keys
for states in capitals:
    print(states,end=' ')
#output Maharashtra
######## Accessing both keys and values 
capitals={"Maharashtra":"Mumbai","UP":"Lacknow","AP":"Hydrabad"} 
for states in capitals:
    print(states,end=' ')
    print(capitals[states])
    
##Values,keys and Items
capitals={"Maharashtra":"Mumbai","UP":"Lacknow","AP":"Hydrabad"}
print(capitals.values())
print(capitals.keys())
print(capitals.items())
#output dict_values(['Mumbai', 'Lacknow', 'Hydrabad'])
#dict_keys(['Maharashtra', 'UP', 'AP'])
#dict_items([('Maharashtra', 'Mumbai'), ('UP', 'Lacknow'), ('AP', 'Hydrabad')])

#########checking key membership
print("AP" in capitals)
print("Bihar" not in capitals)
#True
#True

#Obtaining the length of dictionary
capitals={"Maharashtra":"Mumbai","UP":"Lacknow","AP":"Hydrabad"}
print(len(capitals))

###dictionaries can have values in tuple
seasons={"Summer":('Feb','Mar','Apr','May'),
"Rainy":("June","July","August","Sept"),
"Winter":("Oct","Nov","December","January")}
print(seasons['Rainy'])
print(seasons['Rainy'][0])
###output ('June', 'July', 'August', 'Sept')
#June

#########dictionary methods
#get() is a useful method to access the
#dictionary cannot have 2 items with the same key

#key:
dic={
     "brand":"Maruti",
     "model":"Breeza",
     "year":2021,
     "year":2020
     }
print(dic)
#output {'brand': 'Maruti', 'model': 'Breeza', 'year': 2020}

######loop through a dictionary,it will show only keys
dic={
     "brand":"Maruti",
     "model":"Breeza",
     "year":2021,
     "year":2020
     }
for x in dic:
    print(x)
#brand
#model
#year
for x in dic:
    print(dic[x])
#output
#Maruti
#Breeza
#2020

#########write a python program to add all the items in the list
def sum_list(items):
    sum=0
    for x in items:
        sum=sum+x
    return sum
print(sum_list([1,2,3,4,5]))
