'''Q1)Write a python program to check if a list is empty'''

lst = [1,2,3]
count = 0
for i in lst:
    if i :
        count+=1
if count>=1:
    print("Not empty")
else :
    print("Empty")
    

'''Q2)using list comprehenshion construct a list from the sqaures
of each element in the list'''
list1=[1,2,3,4,5]
lst=[x*x for x in list1]
print(lst)


'''Q3)write a python script to check whether a given key is 
already exists in a dictionary'''
dic={'Name':'Hello','Age':21,'City':'Kopargaon','Branch':'ECE'}
def check(d,k):
    x = dic.keys()
    for i in x:
        if i == k:
            return "Key Exist"
            break
    return "Not exist"
a = check(dic,'Age')
print(a)


'''Q4)create a range from 100 to 160 with steps of 10 second,using
dict comprehension create a dictionary where each number in the range
is the key and each item divided by 100 is the value'''

number = range(100, 161, 10)
result_dict = {num: num / 100 for num in number}
print(result_dict)



'''Q5)create a dataframe which comprises course,fees, and duration and add
tutors column'''
import pandas as pd
df={'course':['java','python','sql','AI'],
    'fees':[10000,20000,30000,23000],
    'duration':['20days','30days','40days','10days']}
df1=pd.DataFrame(df)
tutor = ['abc',"pqr","xyz","mno"]
df1["TUTORS"]=tutor
print(df1)



'''Q6)You have already created dataframe write it to csv'''
import pandas as pd
df={'course':['java','python','sql','AI'],
    'fees':[10000,20000,30000,23000],
    'duration':['20days','30days','40days','10days']}
df1=pd.DataFrame(df)
df1.to_csv("data.csv")



'''Q7)write a python program that return multiple values'''

'''Q8) write a function which takes two argument:a and b and return
multiplication of them'''

def mul_values(x,y):
    return x*y
a = int(input("Enter 1nd Number : "))
b = int(input("Enter 2nd Number : "))
print(mul_values(a,b))

#OR
x = lambda x,y :[x*y]
print(x(2,3))


'''Q9)write a numpy program to test if any of the element of a given
array are non-zero'''
import numpy as np
x=np.array([0,1,2,3,4])
print(x)
print(np.any(x))



'''Q10)write a python program to plot two or more
 lines and set the line marker'''
import matplotlib.pyplot as plt 
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3.0 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])
plt.show()


'''Q11)write a python programming to display a bar chart 
of the popularity of programming languages
sample data:
    programming languages:java,python,php,javascript,c#,c++
    popularity:22.2,23.7,8.8,8,7.7,6.7'''

import matplotlib.pyplot as plt
plt.bar(['python','java','php','javascript','c#','c++'],[22.2,23.7,8.8,8,7.7,6.7]) 
plt.title("Popularity of programming lanaguages")
plt.show()