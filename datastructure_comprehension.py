
#ADVANCED PYTHON
###List Comprehension######

###Normal way
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#By using list comprehension##########
lst=[num for num in range(0,20)]
print(lst)
###output[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

####capitalize() used for making 1st letter capital
name=['dada','kaka','mama']
lst=[name.capitalize() for name in name]
print(lst)

###output ['Dada', 'Kaka', 'Mama']

####list comprehension using if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)
###output [0, 2, 4, 6, 8]
##########################

#creating an identical list from 1st list using list comprehension
list1=[1,2,3,4,5]
lst=[num ++2 for num in list1]
print(lst)

####################################################
#********SET COMPREHENSION**********************

set1={x for x in range(3)}
print(set1)
#output {0, 1, 2}

#*************DICTIONARY COMPREHENSION**********
dict={x:x*x for x in range(3)}
print(dict)

##first create a range from 100 to 160 with steps of 10 using dict comprehension
dict1={x:x+10 for x in range(100,160)}
print(dict1)

#write python program to read entire text file
s=':c'
