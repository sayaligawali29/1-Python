# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:42:32 2023

@author: user
"""

#####Exception Handling######
##Error 
#signifies a situation that mostly happens due to
#absence of system resources
##Exception
##Issues that can appear at runtime and compile
##It majorly arises in code or program

###Exception are hamdled with try-except block
##Handling the ZeroDivisionError Exception
print(5/0)
#Exception occurs
#ZeroDivisionError: division by zero

###Usind try-except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
#####Handling the FileNotFoundError Exception
#encoding='utf-8' is standard encoding technique 
filename='alice.txt'
with open(filename,encoding='utf-8') as f:
    contents=f.read()
##output FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

###Handled in try-except block
file_name='alice.txt'
try :
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")

##JSON javascript object notation
#format was orginally developed for javascript
#JSON file is in the form of dictionary

import json
numbers=[2,3,4,5,7,11]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
    
    
###Saving data with json is useful
#When u are working with user generated data
import json
username=input("What is your name?")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f,"We will remember u,{username}!")


#write a program to whose name has already been stored
import json
filename='username.json'
with open(filename) as f:
   username= json.load(f)
print(f"Welcome back {username}!")
##output Welcome back  Sayali!

####load the username,if it has been stored previously
#otherwise,prompt for the username and store it
filename='username.json'
try:
    with open(filename) as f:
       username= json.load(f)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename) as f:
       username= json.load(f)
       print(f,"We will remember u,{username}!")
else:
    print(f"Welcome back {username}!")
#Welcome back  Sayali!
       
        
