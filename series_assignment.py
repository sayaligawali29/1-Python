#write a pandas program to create and display a one dimensional 
#containing an array of data

import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)
###################################
#write a pandas program to convert a panda module series
#to python list and its type

import pandas as pd
ds=pd.Series([2,4,6,8,10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python List")
print(ds.tolist())
print(type(ds.tolist()))

##Write a pandas program to add,substract,multiple and divide
#sample series:
    #[2,4,6,8,10],[1,3,5,7,9]
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,6,9])
ds=ds1+ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds=ds1-ds2
print(ds)
print("Multiply two series:")
ds=ds1*ds2
print(ds)
print("Divide series by series2")
ds=ds1/ds2
print(ds)


## Write a pandas program to compare to elements of the series
#sample series:[2,4,6,8,10],[1,3,5,7,10]
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1==ds2)
print("Greater than:")
print(ds1>ds2)
print("less than:")
print(ds1<ds2)

##write a pandas program to convert a dictionary to a pandas
#to pandas series
#original dictionary:
#{'a':100,'b':200,'c':300,'d':400,'e':800}
import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':800}
print("Original dic")
print(d1)
new_series=pd.Series(d1)
print("COnverted series:")
print(new_series)

##Write a pandas program to convert a NumPy array 
#to a pandas series
import numpy as np
import pandas as pd
n_a=np.array([10,20,30,40,50])
print("NumPy array:")
print(n_a)
new_series=pd.Series(n_a)
print("Converted Pandas series:")
print(new_series)

#write a pandas program to change the data type 
import pandas as pd
s1=pd.Series(['100','200','Python','300.12','400'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2=pd.to_numeric(s1,errors='coerce')
print(s2)

##write a pandas program to convert the first column of a 
#dataframe as a series

import pandas as pd
d={'col1':[1,2,3,4,7,11],
   'col2':[4,5,6,9,5,0],
   'col3':[7,5,8,12,1,11]}
df=pd.DataFrame(data=d)
print("Original Data")
print(df)
#all rows and 0th column
s1=df.iloc[:,0]
print("\n The column as a series")
print(s1)

###################################################
import pandas as pd
s=pd.Series([['Red','Green','White'],
            ['Red','Black'],['Yellow']])
print("Original Series of list")
print(s)
s=s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)
######or

import pandas as pd
s=pd.Series([['Red','Green','White'],
            ['Red','Black'],['Yellow']])
print("Original Series of list")
print(s)
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print("One Series")
print(s3)

#DataFrame -stack() function

##stack() function is used to stack the prescribed level
#from column to index

#Write a pandas program to add some data to an existing series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("Original Data Series:")
print(s)
print("\n Data Series after adding some data:")
new_s=pd.concat([s,pd.Series([500,"php"])],ignore_index=True)
print(new_s)

##################################################
#write a pandas program to sort a given series.
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("Original Data Series:")
print(s)
new_s=pd.Series(s).sort_values()
print(new_s)
#######################################
#write a pandas program to change the order of index of given series

import pandas as pd
s=pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print("Original Data Series:")
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)
