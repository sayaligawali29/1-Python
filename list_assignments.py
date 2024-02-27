# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 02:02:16 2023

@author: user
"""

#########write a python program to add all the items in the list
def sum_list(items):
    sum=0
    for x in items:
        sum=sum+x
    return sum
print(sum_list([1,2,3,4,5]))
###another way to print sum of 
list1=[1,2,3,4,5]
print(sum(list1))

##write python program to multiply all the elements of the list
def mul_list(items):
    mul=1
    for x in items:
        mul=mul*x
    return mul
print(mul_list([1,2,3]))

#or
list1=[1,2,3]
mul=1
for x in list1:
    mul=mul*x
print(mul)

 ## output 6

###Addition

list1=[1,2,3]
sum=0
for x in list1:
    sum=sum+x
print(sum)
list2=[1,2,3]
x=sum(list2)
print(x)
###write python program to get largest number  in the list
list1=[1,2,3,4,5]
max(list1)
## output 5

##another way
def max_list(items):
    max=list[0]
    
#write a python program to count strings which statisfies the condition that string length is 
#is  2 or more and the first and last characters should be same
list1=['aba','xyz','aba','1221']
count=0
def words_match(words):
    count=0
    for letter in list1:
        count=count+1
        if len(letter)>2 and letter[0]==letter[-1]:
            print(letter,"Matched")
words_match(list1)

##write a python program to get a list ,sorted in increasing
#order by the element in each tuple from a given list of non-empty tuples
list1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def last(n):
    return n[-1]
def sort_list(tuples):
    res=sorted(tuples,key=last)
    return res
print(sort_list(list1))
##output [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
##write a program to remove duplicates from list
list1=[10,20,30,20,10,50,60,40,80,50,40]
dup_items=set()
dup_list=[]
for x in list1:
    if x not in dup_items:
        dup_list.append(x)
        dup_items.add(x)
print(dup_list)
##output [10, 20, 30, 50, 60, 40, 80]

##or
list1=[10,20,30,20,10,50,60,40,80,50,40]
set1=set(list1)
#set remove duplicates items ,list is converted into set
list2=list(set1)
print(list2)

##write a python program to clone or copy a list
list1=[10,22,44,23]
new_list=[]
for item in list1:
    new_list.append(item)
print(new_list)

##write a python program to find the list of words 
#that are longer than n from a given list of words
def long_words(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jumps over the lazy dogs"))
##output ['quick', 'brown', 'jumps', 'over', 'lazy', 'dogs']

##write a  python  function that takes two list and return
#True if they have at least one common members

def common_data(list1,list2):
    res=False
    for x in list1:
        for y in list2:
            if x==y:
                res=True
                return res
print(common_data([1,2,3,4,5],[5,6,7,8]))
print(common_data([1,2,3,4,5],[6,7,8]))

####write python program to calculate the difference betwwn 2 list
list1=[1,2,3,4,5]
list2=[1,4,6,7,9]
diff1= list(set(list1)-set(list2))
diff2= list(set(list2)-set(list1))
tot_diff=diff1+diff2
print(tot_diff)
#output [2, 3, 5, 9, 6, 7]

###write a python to convert a list of characters into a string
##.join() is used to convert characters into string
s=['a','b','c','d']
str1=''.join(s)
print(str1)
##output abcd

##write a python program to find the index of an item in list
num=[10,20,30]
print(num.index(30))
##output 2
##used in recommendation engine

##write python program to append a list to second list
list1=[1,2,3,4]
list2=['Red','Black','Green']
final_list=list1+list2
print(final_list)
##output 1, 2, 3, 4, 'Red', 'Black', 'Green']