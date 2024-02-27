# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 20:14:56 2023

@author: user
"""
##elif statement
savings=float(input("Enter how much you have in savings:"))
if savings==0:
    print("Sorry no savings")
elif savings==500:
    print("Well done")
elif savings==1000:
    print("That's tidy sum")
elif savings==10000:
    print("Welcome")
else:
    print("Thank you")
    
##While Looping
##is used to iterative statment
count=1
print("Start")
while count<=10:
    print(count)
    count+=1

#For loop
print("Print out values in a range")
for i in range (2,10):
    print(i)
    print('Done')

#conditional statement with for loop
n=int(input("Enter the number:"))
for i in range(0,16):
    if i==n:
        break
    print(i)
print("Done")

#Now use an 'anonymous' loop variable
#in python anonymous variable is "_" 
#instead of using i,j,k use _
for _ in range(0,10):
    print("*",end='')
    print()

for _ in range(0,10):
    print("*",end=' ')
    
#Break Loop Statement
n=int(input("Enter number:"))
for i in range(0,5):
    if i==n:
        break
    print(i,' ',end=' ')
print("Done")
#output 1-4 and done

#place of print is changed
n=int(input("Enter number:"))
for i in range(0,5):
    if i==n:
        break
    print(i,' ',end=' ')
    print("Done")
#output 1-4 continue done

#to find odd numbers
#important regarding interview point of view
s,e=4,19
for n in range(s,e+1):
    if(n%2!=0):
        print(n,end=" ")

#to find even numbers
s,e=4,19
for n in range(s,e+1):
    if(n%2==0):
        print(n,end=" ")
        print()
#to find even numbers using increment
s,e=4,20
for i in range (s,e,2):
    print(i,end=" ")
    print()
    
#to find odd numbers using increment
s,e=1,20
for i in range (s,e,2):
    print(i,end=" ")
    print()

#user input for even numbers
s=int(input("Enter start:"))
e=int(input("Enter end:"))
for i in range(s,e+1):
    if i%2==0:
        print(i,end=' ')
        print()

#user input for odd numbers
s=int(input("Enter start:"))
e=int(input("Enter end:"))
for i in range(s,e+1):
    if i%2!=0:
        print(i,end=' ')
        print()
        
#Leap year
#century year we need to divide it by 400
#Non century year we need to divide it by 4
#If year is not divided by 100 means it is not a century

year=int(input("Enter the year:"))
if year%400==0 or year%100!=0 and year%4==0:
    print("Leap Year")
else:
    print("Not a leap year")
##OR
def is_leap_year(year):
    if((year>0) and (year%4==0) and (year%100) and (year%400)):
        return True
    return False
print(is_leap_year(2000))
        
    
#prime number
s=int(input("Enter start:"))
e=int(input("Enter end:"))
for n in range(s,e+1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)

####OR
def prime_num(n):
    for i in range (2,n):
        if(n%i==0):
            return "Not Prime"
            break;
    return "Prime"
prime_num(11)
#Palindrome String
#:: use for slicing of string or
# reversing the string
user_input=input("Enter string:")
rev=user_input[::-1]
if(rev==user_input):
    print("Palindrome")
else:
    print("Not Palindrome")
    

# * Pattern Printing
#for box pattern
# * * *
# * * *
# * * *
for i in range(4):
    for j in range (4):
        print(" *",end=' ')
    print()
#inverted pattern
#*
#* *
#* * *
for i in range(4):
    for j in range (i+1):
        print(" *",end=' ')
    print()
#Mario Pyramid
# * * * 
# * *
# *
for i in range(4):
    for j in range (4-i):
        print(" *",end=' ')
    print()
###Initialization
x,y,z=5,6,7
print(x)
print(y)
print(z)

##Global Variable
x="Best"
def my_function():
    print("Python is "+x)
my_function()

###Global and local variable
x="Best"   #gobal
def my_function():
    x="Good"#local
    print("Python is "+x)
my_function()
print("Python is "+x)

###Dictionary
x={"name":"Sayali","age":34}
print(type(x))

##String and integer concatination is not possible
str1="Hello"
str2=56
str3=str1+str2

#multiple strings
x="""Hello I am Sayali.I am doing python"""
print(x)
x="""Hello I am Sayali.
I am doing python"""
print(x)

#slicing
x="Sayali Gawali"
print(x[7:13])

x="Sayali Gawali"
print(x[:6])

x="Sayali Gawali"
print(x[6:])

#Negative Indexing
x="Sayali Gawali"
print(x[-5:-2])

#modify string
#upper  fun
x="Sayali Gawali"
print(x.upper())
#lower fun
x="Sayali Gawali"
print(x.lower())

#to remove whitespaces strip() fun is used
x="    Sayali Gawali"
print(x.strip())
#output Sayali Gawali

#use replace string
x="Hello Sayali"
print(x.replace("Hello","Hii"))
#output Hii Sayali

#split() which replace white space
x="Sayali,Gawali"
print(x.split(","))
#output ['Sayali', 'Gawali']

x="Sayali Gawali"
print(x.split(" "))
#output ['Sayali', 'Gawali']

#Slicing ::(start to end)
x="Sayali Gawali"
a=x[::-1]
print(a)
#output ilawaG ilayaS reverse string

x="Sayali Gawali"
a=x[::-2]
print(a)
# output iaa lyS difference of 2 character

#find method searches the string for a specified
#value and return the position
x="Sayali Gawali"
print(x.find("ali"))
#output 3

#string concatenation
a="Sayali"
b="Gawali"
print(a+b)
#output SayaliGawali

#to add white space
print(a+" "+b)
#output Sayali Gawali

#string format
a=75
b="Sayali"
#print(a+b)
print(f"my name is Sayali and my age is {a}")
#output my name is Sayali and my age is 75
#number manipulation using fstring

#if u want to display multiple numbers use f string
a=10
b=20
c=60
print(f"I want {a} piece and item number is {b},its price is {c}")

#output I want 10 piece and item number is 20,its price is 60
#other method
a=10
b=20
c=60
z="I want {} piece and item number is {},its price is {}"
print(z.format(a,b,c))

#can pass argument in breces
a=10
b=20
c=60
z="I want {0} piece and item number is {1},its price is {2}"
print(z.format(a,b,c))

#escape character allows you to use double quote
a="I am \"Sayali\""
print (a)

#operator precedence
#PEMDAS
#P parathesis
#E Exponential
#M Multiplication
#D Division
#A Addition
#S Substraction
print(3*3+3/3-3)
#output 7.0
