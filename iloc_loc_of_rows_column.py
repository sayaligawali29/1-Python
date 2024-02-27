#pandas select rows and column use iloc and loc
import pandas as pd

technologies={'Courses':["Spark","Pyspark",None,"Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

#df.iloc[startrow:endrow,startcolumn:endcolumn]

df=pd.DataFrame(technologies,index=row_labels)
#below are quick example
df2=df.iloc[:,0:2]
df2
#this line uses the slicing operator to get the diiference
#item by index
#the first slice[:] indicates to return all rows
#the second slice specifies that only columns
#between 0 and 2 (excluding 2) should be returned

df=pd.DataFrame(technologies)
df2=df.iloc[0:2, :]
df2
#inthis case, the first slice[0:2] is requesting only rows
#o through 1 of the dataframe
#the second slice 

#Slicing specific rows and column using iloc
df3=df.iloc[1:2,1:3]
df3

#the second operator [1:3] yeilds columns 1 and 3
#Select rows by integer index

df2=df.iloc[2] #select row by index
df2
df2=df.iloc[[2,3,6]]#select rows by index list
df2=df.iloc[1:5] # select rows by integer index range
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]# select first 3 rows
df2=df.iloc[-1:]# select last row
df2=df.iloc[-3:]# select last 3 rows
df2=df.iloc[::2]# select alternate rows

########################################################
#Select rows by index labels
df2=df.loc['r2'] # select row by label
df2=df.loc[['r2','r3','r4']] #select rows by index 
df2=df.loc['r1':'r4']  # slect rows by label index
df2=df.loc['r1':'r4':2]#select alternate rows 

########################################################
import pandas as pd

technologies={'Courses':["Spark","Pyspark",None,"Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

#using loc[] to take column slices
#loc[] syntax to clic columns
#df.loc[:,start:stop:step]
#seelct multiple columns
df2=df.loc[:,["Courses","Fee","Duration"]]
#select random columns
df2=df.loc[:,["Courses","Fee","Duration"]]
#select columns between two columnd
df2=df.loc[:,'Duration':]
################################################
import pandas as pd

technologies={'Courses':["Spark","Pyspark",None,"Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
######################################################

##pandas.Dataframe.query() by examples
#query all rows with courses equals 'Spark'
df2=df.query("Courses=='Spark'")
print(df2)

############################
#not equals condition
df2=df.query("Courses!='Spark'")
df2

###############################################
import pandas as pd

technologies={'Courses':["Spark","Pyspark",None,"Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}

df=pd.DataFrame(technologies,index=row_labels)
print(df)

######
#pandas add column to dataframe
#add new column to the dataframe
tutors=['Ram','Sham','Ghanshan','Ganesh','Ramesh']
df2=df.assign(TutorsAssigned=tutors)
print(df2)

##################################################
#add multiple columns to the dataframes
MNCCompanies=['Tata','HCL','Infosys','Google','Amazon']
df2=df.assign(MNC=MNCCompanies,tutors=tutors)
df2
###################################################
#derive new column from existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x:x.Fee * x.discount/100)
print(df2)

####################################################
#Append column to existing pandas dataframe
#Add new column to the existing dataFrame
df=pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
print(df)

####################################################
#Add new column at the specific position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)
###############################################
#Quick Examples of Get the Number of Rows in DataFrame
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count
######################################################
df=pd.DataFrame(technologies)
row_count=df.shape[0]#return number of rows
col_count=df.shape[1]#return number of columnd
print(row_count)
print(col_count)

###################################################
#using dataframe.apply() to apply function add column
import pandas as pd
import numpy as np
data={"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
def add_3(x):
    return x+3
df2=df.apply(add_3)
print(df2)
#another way
df9=df.A.apply(add_3)
print(df9)

###########################
#using apply function single column
def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)
df['B']


##########################################
#Apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_4)
print(df[['A','B']])

#################################################
#apply a lambda function to each column
df1=df.apply(lambda x:x+10)
print(df1)
###################################################
###apply function on selected list of multiple columns

df=pd.DataFrame(data)
df['A']=df['A'].apply(lambda x:x-2)

##################################################
#using pandas.Dataframe.transform() to apply function column
#using dataframe.transform()
def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)
####################################################
#Using pandas.Dataframe.map() to single column
df['A']=df['A'].map(lambda A:A/2)
print(df)

###################################################

#Using Numpy function on single column
#using Dataframe.apply() &[] operator

import numpy as np
df['A']=df['A'].apply(np.square)
print(df)
#############################
#Using NumPy.Square() method
#using numpy .square() and [] operator
df['A']=np.square(df['A'])
print(df)

####################################
#Pandas groupby() with examples
import pandas as pd

technologies={'Courses':["Pyspark","Pyspark","Pandas","Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
df=pd.DataFrame(technologies)
print(df)
#use groupby() to compute the sum
#When theie is repeated entries use groupby
#group by for single column
df2=df.groupby(["Courses"]).sum()
print(df2)

##groupby for multiple columns
df2=df.groupby(['Courses','Duration']).sum()
print(df2)

##################################################
#Add index to the grouped data
#Add Row Index to the group by result
df11=df.groupby(['Courses','Duration']).sum().reset_index()
print(df11)

################################################

#pandas get column names from dataframe
import pandas as pd

technologies={'Courses':["Spark","Pyspark",None,"Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
df.columns
#get the list of all column names from headers
column_headers=list(df.columns.values)
print("The Column Header:",column_headers)
