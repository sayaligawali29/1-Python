# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 02:04:34 2023

@author: user
"""

#find all of the numbers from 1-1000 that is divisible by seven
div7=[n for n in range(1,1000) if n%7==0]
print(div7)

##############################
#find all the numbers from 1-1000 that have 3 in them
lst=[n for n in range(1,1000) if '3' in str(n)]
print(lst)

#############################
lst=[f"{x}{y}" for x in range(3) for y in range(3)]
print(lst)

##output['00', '01', '02', '10', '11', '12', '20', '21', '22']
#####################


#count the number of spaces in string
some_string='the slow solid squid swam sumptuously through the slimy swamp'
spaces=[s for s in some_string if s==' ']
print(len(spaces))
#output 9


##Create a list all the consonants in the string
#'Yellow Yaks like yelling and yawning and yesturday they yodled whilw eating yuky yams

sentence='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
result=[letter for letter in sentence if letter not in 'a,e,i,o,u ," "']
print(result)

########################
#find the common number in two list
#without using tuple or set)list

list_a=[1,2,3,4,5]
list_b=[2,3,4,6,7]
common=[a for a in list_a if a in list_b]
print(common)
#output 
#[2, 3, 4]

###Get only the numbers in a sentence like 'In 1984 there were 13 instances of a protest with over 1000 people attending'
#isalpha() method returns True if all the characters are alphabet letters (a-z).
sentence='In 1984 there were 13 instances of a protest with over 1000 people attending'
words=sentence.split()
result=[number for number in words if not number.isalpha()]
print(result)
#output ['1984', '13', '1000']

##Given number =range(20),produce a list containing the word 'even'

for n in range(20):
    if n%2==0:
        print('even')
    else:
        print('odd')
print(result)

###using list comprehension
result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)

###produce a list of tuples consisting of only
#the matching numbers in these lists list_a=[1,2,3,4,5,6,7,8],
#list_b=[2,7,1,12] result would like (4,4),(12,12)

list_a=[1,2,3,4,5,6,7,8]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a==b]
print(result)

#######sentence assignment#######################

s1='Hi i am sayali'
s2='Hi i am pranav'
examine=s1.split()
examine1=s2.split()
result=[(word,word1) for word in examine for word1 in examine1 if word==word1]
print(result)

#output [('Hi', 'Hi'), ('i', 'i'), ('am', 'am')]



#Find all of the words in a string that are less than
#4 letters
sentence='On a summer day Ramnath sonar went swimming in the sun and his red skin stung'
examine=sentence.split()
result=[word for word in examine if len(word)<=4]
print(result)
#output ['On', 'a', 'day', 'went', 'in', 'the', 'sun', 'and', 'his', 'red', 'skin']


#write a python program to print a specified list
#after removing the 0th,4th, 5th elements
color=['Red','Green','White','Black','Pink','Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
#output ['Green', 'White', 'Black']

#write a python program that create generator function
#thst yeilds a cube of numbers from 1 to n
#accept n from user

def cube_generator(n):
    for i in range(1,n+1):
        yield i**3
#accepting from user
n=int(input("Enter number:"))
#create the generator object
cubes=cube_generator(n)
#iterate over the generator object
for num in cubes:
    print(num)

#write a python program to implement a generator that
#generates random numbers within a given range
import random
def random_number_generator(start,end):
    while True:
        yield random.randint(start,end)
        
#accept from user
start=int(input("Enter start:"))
end=int(input("Enter end:"))
#generator object
random_numbers=random_number_generator(start,end)
print("Random numbers between",start,"and",end)
for _ in range(10):
    print(next(random_numbers))
##list comprehension for multidimentional array
#write a python program to generate a 3*4*6 3D array
#whose each element id *
array=[[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

#write a python program to print the number of specified list
#after removing even numbers from it

num=[7,8,120,25,44,20,27]
num=[x for x in num if x%2!=0]
print(num)
# ouput [7, 25, 27]