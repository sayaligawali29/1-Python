# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#functions

def prime_number(num):
    for i in range(2,num):
        if(num%i==0):
            return "not prime"
            break
        return"prime"
print(prime_number(11))       
#output  prime

##########################

###function without arugument

def greet_user():
    print("Hello")
greet_user()


#passing information to function
def greet_user(username):
    print(f"Hello,{username}!")
greet_user("Sayali")
#output Hello,Sayali!

###positional arugument
#order matters in positional arugument
def describe_pet(animal_type,pet_name):
    print(f"\nI havr a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name}.")
describe_pet('Cat', 'Mau')

#default values
def describe_pet(pet_name,animal_type='Cat'):
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name= 'Mau')

#I have a Cat.
#my Cat's name is Mau.

#avoiding aurgument Errors
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name= 'Mau')

# Assignment no 2

#1 rollar coastar

height=int(input("Enter a height: "))
if height>=120:
    print("U are eligible to play rolar coastar")
    age=int(input("Enter a age:"))
    if age<18 and height>120:

        print("Ticket will be 20rs")
    elif age>18:
        print("Ticket will be 50rs")
    elif age == 12:
        print("Ticket will be 10rs")
    elif  12<=age<=18 and height==120:
        print("Ticket is 15rs")
else:
    print("You are not eligible to play rolar coastar")
########OR
print("Welcome tp roller coaster")
height=int(input("Enter a height: "))
bill=0
if height>=120:
    print("U are eligible to play rolar coastar")
    age=int(input("Enter a age:"))
    if age<12:
        print("5 Rs")
        bill=5
    elif age<=18:
        print("10 Rs")
        bill=10
    else:
        print("15 Rs")
        bill=15
    want_photo=input("Do you want photo Y or N:")
    if want_photo=='Y':
        bill+=3
        print(f"Your total bill will be{bill}")
    else:
        print(f"Your total bill is {bill}")
else:
    print("Sorry not eligible")


    
#############
def days_left(age):
    age_left=80-age
    days=365*age_left
    weeks=52*age_left
    months=12*age_left
    return f"You have {days} days, {weeks} weeks, {months} months remained"
age=int(input("Enter your age"))
print(days_left(age))

########
users=["Admin","Employee","Manager","Worker","Staff"]
for user in users:
    if user=="Admin":
        print("Hello Admin")
    elif user=="Employee":
        print("Hello Employee")
    elif user=="Manager":
        print("Hello Manager")
    elif user=="Worker":
        print("Hello Worker")
    else:
        print("You are not member of company")
        
########Password Picker########
import string
#pick Adjectives
adj=["Red","Orange","Green","Blue","Purple"]
#pic noun
noun=["Apple","Mango","Orange","Pineapple","Banana"]
#pick the words
import random
adj=random.choice(adj)
noun=random.choice(noun)
#select a number
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
#create the new secure password
password=adj+noun+str(number)+special_char
print("Your new password is: %s"% password)

######
while True:
    adj=random.choice(adj)
    noun=random.choice(noun)
    #select a number
    number=random.randrange(0,100)
    #select a special character
    special_char=random.choice(string.punctuation)
    #create the new secure password
    password=adj+noun+str(number)+special_char
    print("Your new password is: %s"% password)
    res=input("Would u like to generate another password? type y or n:")
    if res=='n':
        break
###orangeblue1
    
###write python to check password is good or not
#it must at least 8 character
#one upper case
# one lower code

def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    for c in password:
        if c>="A" and c<="Z":
            has_upper=True
        elif c>="a" and c<="z":
            has_lower=True
        elif c>="0" and c<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
    
password=input("Enter password:")
#checkPassword(password)

if checkPassword(password):
    print("Strong Password")
else:
    print("Weak Password")
    
###output Strong or weak password


####calculate age
print("What is ur todays age")
years_today=input("Years:")
months_today=input("Months:")
days_today=input("Days:")
tot_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"Ypor total age today in days {tot_days_today}")
print("Let us assume you are expected to live 90 years")
tot_days_to_live=90*365
remaining_days_to_live=tot_days_to_live-tot_days_today
print(f"Your remaining life in days {remaining_days_to_live}")

 ######Calculate pizza order bill
print("Welcome to Pizza Hut")
pizza_size=input("Enter size of pizza (S,M,L):") 
num_pizza=int(input("How many pizza??"))
bill=0
if pizza_size=="S":
    bill=15
    print("Small Size Pizza")
elif pizza_size=="M":
    bill=20
    print("Medium Size Pizza")
elif pizza_size=="L":
    bill=25
else:
    print("Invalid Input")
add_pep=input("Do you want to add Pepproni(Y/N):")
add_cheez=input("Do you want to add extra cheez(Y/N):")
if(add_pep=="Y" and pizza_size=="S"):
    bill+=2
elif(add_pep=='Y'and (pizza_size=="M" or pizza_size=="L")):
    bill+=3
if(add_cheez=="Y"):
    bill+=1
    print(f"Your bill is ${bill*num_pizza}")
else:
    print(f"Your bill is ${bill*num_pizza}")
    
    
#####function Returning Dictionary###
def person_name(first_name,last_name):
    ##returning the dictionary
    person={"first":first_name,"last":last_name}
    return person
print(person_name("Sayali","Gawali"))
###output {'first':'Sayali','last':'Gawali'}

#####Passing a list######
#.title()returning string
def greet_person(user):
    for name in user:
        msg=f"Hello,{name.title()}!"
        print(msg)
list_name=["Sayali","Shweta"]
greet_person(list_name)

####Passing an Arbitrary number of Arguments
#if u want to add multiple argument then *is used before argument
def make_pizza(*topping):
    print(topping)
make_pizza("pepproni")
make_pizza("Black Paper","Extra Cheeze","Paneer")
#output ('pepproni',)
#('Black Paper', 'Extra Cheeze', 'Paneer') inthe form of tuple

def make_pizza(*toppings):
    print("Make the pizza by following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza("pepproni")
make_pizza("Black Paper","Extra Cheeze","Paneer")
##output Make the pizza bt following toppings:
#-pepproni
#Make the pizza bt following toppings:
#-Black Paper
#-Extra Cheeze
#-Paneer

####mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    print(f"\nMaking the {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(17,"pepproni")
make_pizza(15,"Black Pepper","Extra Cheeze","Paneer")
#output
# Making the15-inch pizza with following toppings:
#-Black Paper
#-Extra Cheeze
#-Paneer
###importing file
import pizza
pizza.make_pizza(17,"pepproni")
pizza.make_pizza(15,"Black Pepper","Extra Cheeze","Paneer")

#####Importing Specific Function
from pizza import make_pizza
make_pizza(17,"pepproni")
make_pizza(15,"Black Pepper","Extra Cheeze","Paneer")
# Making the15-inch pizza with following toppings:
#-Black Paper
#-Extra Cheeze
#-Paneer

######Using as to a functions an Alias
from pizza import make_pizza as mp
mp(17,"pepproni")
mp(15,"Black Pepper","Extra Cheeze","Paneer")

#####Using as to give a module an Alias
####alias means giving short name
import pizza as p
p.make_pizza(17,"pepproni")
p.make_pizza(15,"Black Pepper","Extra Cheeze","Paneer")
##Output
# Making the15-inch pizza with following toppings:
#-Black Paper
#-Extra Cheeze
#-Paneer

#####importing all functions in a module
#if we want to import all functions * is used
from pizza import *
make_pizza(17,"pepproni")
make_pizza(15,"Black Pepper","Extra Cheeze","Paneer")

#####Scope of Variable
### we need to intiliaze and then call 
x=x+1
x=6
print(x)
#output NameError: name 'x' is not defined

####Lamda function or Anonymous function
###Addition
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
###15 output
add=lambda a,b,c:a+b+c
add(4,5,6)
###output are same 15

###Multiplication
def mul(a,b,c):
    mul=a*b*c
    return mul
print(mul(4,5,6))
mul=lambda a,b,c:a*b*c
mul(4,5,6)

###using arbitary arguments
val=lambda *args:sum(args)
val(1,2,3,5,6)
val(1,2,3,5,7,8,9)

#############keyword arguments
def person(name ,**data):
    print(name)
    print(data)
person(name="Sayali",age=21,place="Mumbai",mob_no=7350234009)
###output
#Sayali
#{'age': 21, 'place': 'Mumbai'}

######
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name="Sayali",age=21,place="Mumbai",mob_no=7350234009)
###output
#Sayali
#age 21
#place Mumbai
#mob_no 7350234009

###########################
val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)
###25 output

max=lambda a,b:x if (a>b) 
###error expected else
print(max(1,2))

max=lambda a,b:x if (a>b)else b
print(max(8,10))
###output 10


