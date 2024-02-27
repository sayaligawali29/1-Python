#Pandas DataFrame -Basic Operation
#create DataFrame with None/Null to work with examples

import pandas as pd
import numpy as np
technologies={'Courses':["Spark","Pyspark","Pandas",None,"Java"],
              'Fee':[20000,25000,np.nan,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)

###DataFrame properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes

######Accessing one column contents
df['Fee']
###Accessing two columns contents
df[['Fee','Duration']]

#select certain rows and assign it to another dataframe

df2=df[6:]
df2
##Accessing certain cell  from column
df['Duration'][3]

## Substracting specific values from a cloumn
df['Fee']=df['Fee']-500
df['Fee']

#pandas to manipulate Dataframe
#Describe dataframe
#Describe dataframe for all numberic column

df.describe()
#It will show 5 number summery

################################

#rename()-renames pandas Dataframe columns
df=pd.DataFrame(technologies,index=row_labels)
#Assign new header by setting new column name
df.columns=['A','B','C','D']
df

##############################
#rename column names using rename() method

df=pd.DataFrame(technologies ,index=row_labels)
df.column=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})
df2


#######################################################
#drop dataframe rows and column
df=pd.DataFrame(technologies ,index=row_labels)

#drop rows by labels
df1=df.drop(['r1','r2'])
df1

#Delete rows by position/index
df1=df.drop(df.index[1])
df1=df.drop(df.index[[1,3]])

#delete rows by index range
df1=df.drop(df.index[2:])

#when u want have default indexs for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df1=pd.DataFrame(technologies)
df1=df.drop([0,3])#it will delete row0 n row3
df1=df.drop(range(0,2))#it will delete 0 and 1

###################################################3333333
#dropping columns
import pandas as pd

technologies={'Courses':["Spark","Pyspark","Pandas","Java"],
              'Fee':[20000,25000,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}
df=pd.DataFrame(technologies)
print(df)
#drop column by name
#drops 'fee column
df2=df.drop(["Fee"],axis=1)
print(df2)

##explicitly using parameter name labels
df2=df.drop(labels=["fee"],axis=1)

#alternate way
df2=df.drop(column=["fee"],axis=1)

##drop column by index 
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)


##########################################################
#when u are working on original data frame
#inplace=true is mandatory
df.drop(df.columns[1],axis=1,inplace=True)
print(df)
df=pd.DataFrame(technologies)

#drop two or more column by label name
df2=df.drop(["Courses","Fee"],axis=1)
print(df2)

#drop two or more column ny index
df=pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)

#####################################################
#Drop columns from list of columns
df.pd.DataFrame(technologies)
lisCol=["Courses","Fee"]
df2=df.drop(lisCol,axis=1)
print(df2)