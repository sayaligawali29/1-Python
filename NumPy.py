 ##NUMPY#########################
#the numpy library is popular open-source python 
#library used for scientific computing application
#it stands for Numerical Python
#which is consisting of multidimentional array
#objects and a collection of routines for processing




'''Write a python list can contain different data types within a
single list all of the elements in aNumpy array should be homogenus
'''
#Array in NUmpy
#Create nd array

import numpy as np
arr=np.array([10,20,30])
print(arr)
## [10 20 30]

#Create Multidimentional Array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
#[[10 20 30]
# [40 50 60]]

#represent the minimum dimensions
#use ndmin param to specify how many minimum
#dimension you wanted to create an array with dimension
#Minimum dimension

arr=np.array([10,20,30,40],ndmin=3)
print(arr)
#[[[10 20 30 40]]]

#Change the datatype 
#dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)
#[10.+0.j 20.+0.j 30.+0.j]

#gwt the dimension of array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)#2
print(arr)
'''[[ 1  2  3  4]
 [ 7  8  6  7]
 [ 9 10 11 12]]'''

#finding the size of each item in the array
arr=np.array([10,20,30])
print("Each item contain in bytes:",arr.itemsize)
#Each item contain in bytes: 4

###############################################
#get the data type

arr=np.array([10,20,30])
print("Each item contain in type:",arr.dtype)
#Each item contain in type: int32

################################################
#Get the shape and size of array 
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array Size:",arr.size)#Array Size: 8
print("Shape:",arr.shape)#Shape: (2, 4)

###################################################
#create a sequence of integer using arrange()
#from 0 to 20 step of 3

arr=np.arange(0,20,3)
print("A sequential array with steps of 3:\n",arr)
#A sequential array with steps of 3:
# [ 0  3  6  9 12 15 18]

############################################################
#array indexing in numpy
#access single element using index
arr=np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[2])
#2
print(arr[-2])
#9

#########################################################
#multidimensional-dimensional array element 
#using array indexing

arr=np.array([[10,20,30,40,50],[20,30,40,10,30]])
print(arr)
#[[10 20 30 40 50]
 #[20 30 40 10 30]]

print(arr.shape)
#(2,5) now x is 2 dimensional

print(arr[1,1])
#30

print(arr[0,4])
#50
print(arr[1,-1])
#30 

#####################################
#Accessing array elements using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[1:8:2])#start:end:step of 2
#[1 3 5 7]

print(arr[-2:3:-1])#start last but one(-2) upto 3 but not 3 in step of -1
#[8 7 6 5 4]

print(arr[-2:10])#start last but one(-2) and upto 10 but not 10
#[8 9]


#######################################################
#Slicing Array
multi_arr=np.array([[10,20,10,40],[40,50,70,90],
                    [60,10,70,80],[30,90,40,30]])
multi_arr
#Slicing array
#for multidimensional numpy arrays
#you can access the elements as below

multi_arr[1,2]#to access the value at row 1 and column 2
#70
multi_arr[1,:]#to get the value at row 1 and all columns
#array([40, 50, 70, 90])
multi_arr[:,1]#Access the value at all rows and column 1
# array([20, 50, 10, 90])

x=multi_arr[:3,::2]#column frim 0 to 3 in all seleccted rows
print(x)
'''[[10 10]
 [40 70]
 [60 70]]'''
    
################################################
#integer array indexing
#integer array indexing LLOWS THE SELECTION OF ARBITARARY ITEMS
arr=np.arange(35).reshape(5,7)
print(arr)
'''[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]'''
    
#######################################################
#Boolean Array Indexing
#this advanced indexing occurs when an objext
#it is an array object of boolean types,such as may returned from
#comparison operators use the method when we want to pick 
#elements from the array which satisfy spme condition

#Boolean array indexing

arr=np.arange(12).reshape(3,4)
print(arr)
'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''
    
rows=np.array([False,True,True])#not 0th row only first and 
wanted_rows=arr[rows,:]#in selected rows all rows and column
print(wanted_rows)
'''[[ 4  5  6  7]
 [ 8  9 10 11]]'''

#####################################################    
#We can  convert



#create array
array=np.array([10,20,30,40])
print("Array:",array)#Array: [10 20 30 40]
print(type(array))#<class 'numpy.ndarray'>

#If u want to convert array into list
#use .tolist()
lst=array.tolist()
print("list:",lst)#list: [10, 20, 30, 40]
print(type(lst))#<class 'list'>

#####################################################
#convert multidimensional array to list
#create array
array=np.array([[10,20,30,40],[50,60,70,80]
                ,[60,40,20,10]])
print("Arrays:",array)
'''Arrays: [[10 20 30 40]
 [50 60 70 80]
 [60 40 20 10]]'''
    
#convert list
lst=array.tolist()
print("list:",lst) 
'''list: [[10, 20, 30, 40], [50, 60, 70, 80], [60, 40, 20, 10]]'''


##Convert list tp numpy array
#numpy provides us with two functions to use
#when converting a list into array:
    #numpy.array()
    #numpy.asarray()
    
#numpy.array(): 
    
#create list
list=[10,20,30,40]

#convert array
array=np.array(list)
print("Array:",array)
#Array: <class 'list'>

#using numpy.asarray()
#convert array
list=[20,40,60,80]
array=np.asarray(list)
print("Array:",array)#Array: [20 40 60 80]
print(type(array))#<class 'numpy.ndarray'>

#properties
'''ndarray.shape
ndarray.item
ndarray.itemsize
ndarray.ndmin
'''
#ndarray.shape
#to get the shape of python numpy array use numpy.ndarray.shape

#shape 
array=np.array([[1,2,3],[4,5,6]])
print(array)
print(array.shape)
#(2,3)

#numpy reshape():function of this resizing of array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)
'''
[[10 20]
 [30 40]
 [50 60]]'''
###################################################
#Operation using in NUmpy
#NumPy's operation are divided into three main

'''
categories :
    Fouriers Transform  and shape manipulation
    Mathematical and logical operation
    linear algebra and random number generation
'''
'''apply arithematic operation on numpy arrays'''

arr1=np.arange(16).reshape(4,4)
arr2=np.array[1,3,2,4] 