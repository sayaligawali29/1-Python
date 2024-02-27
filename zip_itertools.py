###Use of Zip Function#######
#zip() to integrate the balanced list or combine list
name=['dada','kaka','mama']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
    
####USE OF ZIP FUNCTION WITH MIS MATCH LIST
#zip function ignore excess mismatch item in name
name=['dada','kaka','mama','baba']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

##Zip_longest#######
##to overcome the above drawback the zip_longest is used
#it is imported from itertools
from itertools import zip_longest
name=['dada','kaka','mama','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
#output
#dada 9850
#kaka 6032
#mama 9785
#baba None
    
##Use of fill value instead None
#fillvalue is used to assign the 0 value in place of none
from itertools import zip_longest
name=['dada','kaka','mama','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
#output
#dada 9850
#kaka 6032
#mama 9785
#baba 0

#use of all() ,if all the values are true then it will produce output
lst=[2,3,6,8,9] #values must be non zero,+ve,-ve
if all(lst):
    print("All values are true")
else:
    print("Useless")

############
lst=[2,3,0,8,9] #values must be non zero,+ve,-ve
if all(lst):
    print("All values are true")
else:
    print("Useless")
    
##any() if their is any +ve or -ve values then it will return true

#####USe of any if any one non zero value
lst=[0,0,0,-1,0] #values must be non zero,+ve,-ve
if any(lst):
    print("All values are true")
else:
    print("Useless")
    
##use of any
lst=[0,0,0,0,0] 
if any(lst):
    print("All values are true")
else:
    print("Useless")
#when the list contain all zero then it will return false

####Another itertool count()
#for application perspective this count() is widely use
#count() mostly used in image preocessing
###count() imported from itertool

##count()

from itertools import count
counter=count()
print(next(counter))
print(next(counter))
#output
#0
#1
##Now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))

##Cycle()
#Suppose u have repeated tasks to be done,then cycle() is used

import itertools
instructions=("Eat","Code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)

##repeat()
#it is used for the specific iteration
from itertools import repeat
for msg in repeat("Keep patience",times=3):
    print(msg)
    
##combintions()

from itertools import combinations
players=['John','Jani','Janardhan']
for i in combinations(players,2):
    print(i)
    
#permutation()
from itertools import permutations
players=['John','Jani','Janardhan']
for i in permutations(players,2):
    print(i)
    
#product()
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['Virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)
    
##Filter#########
#filter() is used to filter the entities of list,t,d,s

age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])
#output [27, 21, 19]
