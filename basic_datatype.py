
#21/07/2023

print("Hello world")
x=1
print(x)
print(type(x))
x=100000000001
print(x)

age=input("Enter the age:")
print(type(age))
print(age)

age1=input("Enter the age:")
print(type(age1))
print(age1)

age2=input("Enter the age:")
print(type(age2))
print(age2)

age=age1+age2
print(age)

age1=int(input("Enter the age:"))
print(type(age1))
print(age1)

age2=int(input("Enter the age:"))
print(type(age2))
print(age2)

age=age1+age2
print(age)

exchange_rate=8.55
print(type(exchange_rate))
print(exchange_rate)
##coverting int to float and float to int
int_value=100
string_value='1.5'
float_value=float(int_value)
print("int value as a float:",float_value)
print(type(float_value))
float_value=float(string_value)
print("String value as a float:",float_value)
print(type(float_value))

#complex number
c1=1
c2=2j
print("c1:",c1,"c2:",c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean Numbers

all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

#to convert string into boolean

status=bool(input("Ok it is confirmed?"))
print(status)
print(type(status))

#Arithmetic Operator

home=10
away=15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for=10
goals_against=7
print(goals_for-goals_against)
print(type(goals_for-goals_against))

print(100/20)
print(type(100/20))
# using / result is in float

print(100//20)
print(type(100//20))
# using // result is in integer

print("Modulus division 100%13:",100%13)
print("Modulus of 3%2:",3%2)

#power operator
#for calculating power we use **
a=5
b=3
print(a ** b)

#Assignment Operator

x=0
x+=1
print(x)

#None Value
# is and is not operator is used 
winner=None
print(winner is None)
print(winner is not None)

winner=None
print('Winner:',winner)
print('Winner is None:',winner is None)
print('Winner is not None:',winner is not None)
print(type(winner))
print('Set winner to True')
winner=True

#FLow of control using If Statement
#if statement
n=int(input('Enter a number:'))
if n>0:
    print(n)
    
    
#if-else statement
n=int(input('Enter a number:'))
if n<0:
    print("Negative")
else:
    print("Positive")