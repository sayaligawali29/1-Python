'''write a numpy program to get numpy version and show the numpy
'''
import numpy as np
print(np.__version__)
#1.24.3

'''write a numpy program to test whether none of the elements
of given array are zero'''
import numpy as np
x=np.array([1,2,3,4])
print(x)
print("Test if none of the element is zero:")
print(np.all(x))#True
x=np.array([0,1,2,3])
print(np.all(x))#False

import numpy as np
x=np.array([0,1,2,3,4])
print(x)
print(np.all(x))
''' write numpy program to test if any of the element
given array are non zero'''

import numpy as np
x=np.array([1,0,0,0])
print(x)
print("Test whether any of the elements of given array is non zero:")
print(np.any(x))#true
x=np.array([0,0,0,0])
print(x)
print("Test whether any of the elements of given array is non zero:")
print(np.any(x))#false

'''write numpy program to test a given array element wise for
finiteness(not infinity or not a number)
'''
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original Array")
print(a)
print("Test a given array element wise for finiteness:")
print(np.isfinite(a))
#[ True  True False False]

'''write a numpy program to test element wise for nan of a given
array'''
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original Array")
print(a)
print("Test a given array element wise for NaN:")
print(np.isnan(a))
#[False False  True False]


''' write numpy program to create an element-wise comparison
(greater ,greater equal,less and less_equal)of two given arrays'''
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("Original numbers:")
print(x)
print(y)
print("Comparison-greater")
print(np.greater(x,y))#[ True False]
print("Comparison-greater_equal")
print(np.greater_equal(x,y))#[ True  True]
print("Comparison-Less")
print(np.less(x,y))#[False False]
print("Comparison-less_equal")
print(np.less_equal(x,y))#[False  True]

'''' Write a numpy program to create a 3x3 identity matrix''
'''
import numpy as np
array_2d=np.identity(3)
print('3x3 matrix')
print(array_2d)
'''[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]'''

'''write a numpy program to generate random number between
0 and 1'''
#random.normal() means normally distributed
import numpy as np
rand_num=np.random.normal(0,1,1)
print("Random number betwwen 0 and 1:")
print(rand_num)
#[0.69934757]

'''write a numpy program to create a 3x4  array and iterate
over it'''
import numpy as np 
a=np.arange(10,22).reshape(3,4)
print("Original Array:")
print(a)
print("Each element of array:")
for x in np.nditer(a):
    print(x,end=" ")
    print()
    
''''write a numpy program to create a vector of length 5 with values
evenly distributed between 10 and 50'''
import numpy as np
v=np.linspace(10,49,5)
#10-start point,49-end,5-nos in vector
print("length 5 with values evenly distributed between 10 and 50")
print(v)
#[10.   19.75 29.5  39.25 49.  ]

''' write a numpy program to create a 3x3 matrix with valued
ranging from 2 to 10'''
import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)
'''[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]'''
    
''' write a numpy program to  reverse an array (the first
element becomes the last)'''
import numpy as np
n=np.arange(12,38)
print("Original array:")
print(x)
print("Reverse array:")
x=x[::-1]
print(x)
'''[[ 8  9 10]
 [ 5  6  7]
 [ 2  3  4]]'''
    
''' write a numpy program to compute multiplication of two given matrix'''
#.dot is use to calculate the product of two matrices

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original Matrix")
print(p)
print(q)
result1=np.dot(p,q)
print("Result of matrix multiplication:")
print(result1)
'''[[1 2]
 [3 4]]'''
    
''' write a numpy program to compute cross 
product of two matrices'''
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original Matrix")
print(p)
print(q)
result1=np.cross(p,q)#[ 2 -3]
result1=np.cross(q,p)
print("Result of matrix multiplication:")
print(result1)#[-2  3]

'''write numpy program to compute the determinant of a
given square array'''

import numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-d array:")
print(np.linalg.det(a))
#2.0

'''write a numpy program to compute the eigenvalues
and right eigenvectors of a given sqaure array'''

import numpy as np
m=np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigenvalues of said matrix",w)
#Eigenvalues of said matrix [2. 1.]
print("Eigenvalues of the said matrix",v)

'''Eigenvalues of the said matrix [[0.89442719 0.70710678]
 [0.4472136  0.70710678]]'''

''' write a numpy program to inverse of a given matrix'''
import numpy as np
m=np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result=np.linalg.inv(m)
print(result)
'''[[-2.   1. ]
 [ 1.5 -0.5]]'''
    
''' '''
