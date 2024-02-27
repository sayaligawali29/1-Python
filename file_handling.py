# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:08:02 2023

@author: user
"""
###file is a block of bytes
##################################################
###########*******FILE HANDLING********############
#pi_digits.txt file should be present in working directory
#and present in 1-python
with open('pi_digits.txt') as file_object:
    ##the open()function needs
    #one argument :the name of the file you want to open 
    contents=file_object.read()
print(contents)
##output
#3.1415926535
#8979323846
#2643383279 
with open('programming.txt') as file_object:
    contents=file_object.read()
print(contents)

###rstrip()is used to remove whitespace

##Relative path

with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())
    
##types of path
##1.Relative path(only file name)
##2.Absolute path(whole path i.e c:/1-python/pi_digits.txt)
##when ur going to use absolute path their
# is no need to have working directory

###Absolute Path

file_path='c:/1-python/pi_digits.txt'
with open('pi_digits.txt') as file_object:##loading this file in memory
    contents=file_object.read()
    print(contents.rstrip())
##output
#3.1415926535
#8979323846
#2643383279 

####relative path
##reading line by line

filename='pi_digits.txt'
#we assign the name of the file we are reading from to the variable
with open(filename) as file_object:
    ##we again use the syntax with open and closw python file properly
    for line in file_object:
        print(line)
##output 
#3.1415926535

#8979323846

#2643383279

filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#output
#3.1415926535
#8979323846
#2643383279
#rstrip() is used to remove whitespace

#######Working with a file's contents
#after u read a file into memory
#u can do whatever u want with data
##readlines() is used read lines
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string+=line.rstrip()
        print(pi_string)
        print(len(pi_string))
#output
#3.1415926535
#12
#3.14159265358979323846
#22
#3.141592653589793238462643383279
#32

#ONE SIMPLESR WAYS TO SAVE DATA IS TO WRITE IT
#to a file when u write text to a file
#the output will still be available after
#you close the terminal containing ur program o/p

filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love Programming")
##output will be updated on programming.txt on notepad
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love Programming")
    file_object.write("I love Data Science")
    
##including new line
#write() all existing get remove and new content gets added
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love Programming\n")
    file_object.write("I love Data Science\n")
    
#####Appending to a file
#When u open a file in append mode
##python does nt erase the content of file
##and add the content in it
filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I love AI\n")
    