###Shallow Copies and Deep Copies

#Assignment Operation

#this will only create a new variable for the same reference
list1_a=[1,2,3,4,5]
list_b=list1_a # both are pointing to the same object if 
#we make the changes in one list it is applied to both the list
list1_a[0]=-10
print(list1_a)
print(list_b)

#Shallow Copy
#create one level deep copy
#modifying on level one doesnt affect the other list
#in order create shallow funtion copy() fun of copy module is used
#It is going to create one level instance
#it is imported from copy()

import copy
list1=[1,2,3,4]
list2=copy.copy(list1)
list2[0]=-10
print(list1)
print(list2)


#But with nested objects,modifying on level 2 or
#deeper does not affect the another level list

list_a=[[1,2,3,4,5],[6,7,8,9,10]] 
list_b=copy.copy(list_a)
#affect the other
list_a[0][0]=-10
print(list_a)
print(list_b)

##Deep copies

#full independent clones are created 
#use copy.deepcopy()

import copy
list1=[[1,2,3,4,5],[6,7,8,9,10]] 
list2=copy.deepcopy(list1)
list2[0][0]=-10
print(list1)#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(list2)#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
