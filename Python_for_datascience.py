##PYTHON FOR DATA SCIENCE

#A series is used to model one dimensional data, similar to list
# to a list in python
#the series object also has few more bits
#daya including an index and name
#import pandas 

import pandas as pd 
song2=pd.Series([145,142,38,13],name='counts')
#it is easy to inspect the index of a series (or data)
song2.index
#the index can be string based as well 
#in which case pandas indicates
#that the datatype for the index is object(not string)

song3=pd.Series([145,142,38,13],name='counts',index=['paul','Jacl','jon','tom'])
song3.index
song3

#The NaN value
#this value stands for Not a Number
#and usually ignored in arithmatic (similar to Null in SQL)
#if u load data from a CSV file
#an empty value for an otherwise

#numeric column will become NaN
#if working directory is not selected absolute path should be given
#importing csv.file
import pandas as pd
f1=pd.read_csv('c:/1-Python/age.csv')
f1
##now working directory selected

import pandas as pd
f1=pd.read_csv('age.csv')
f1

##Importing excel file

df=pd.read_excel('c:/1-Python/Bahaman.xlsx')
df

##None,NaN,nan, and null are synonyms
#the series object behave similarly to a NumPy array
#np is alias name of numpy

import numpy as np
numpy_ser=np.array([145,142,38,13])#accesing series element
song3[1]#142
numpy_ser[1]#142

#they both have methods in common
song3.mean()
numpy_ser.mean()



###############################
###PANDAS SERIES DATA STRUCTURE PROVIDES
#SUPPORT FOR THE BASIC CRUD
#operations-create,read,update,and delete
#creation
import pandas as pd
george=pd.Series([10,7,1,22],index=['1968','1969','1970','1970'],name='George songs')
george

#thr previous example explain interesting feature of pandas the index values are string and they
# are not unique.this can cause some confusion,but also be useful
#when duplicate index items are needed

#########Reading

george['1968']

#we can iterate over data in a series
#as well ehrn iterating over a series
for item in george:
    print(item)
    
########Updating

#Updating values in a series can be a little ticky as well
#to update a value for a given index label
#the standard index assignment operation

george['1969']=68
george['1969']

#####Deletion

#the del statement appears to have problems with dup index
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

##Convert Types
#string use .astype(str)
#numeric use pd.to_numeric
#integer use .astype(int)
#note that this will fail with NaN
#datetime use pd.to_datetime
songs_66 =pd.Series([3,'None',11,9],index=['George','Ringo','John','Paul'],name='Counts')
songs_66.dtype
#dtype ('float64)
pd.to_numeric(songs_66.apply(str))#error 
pd.to_numeric(songs_66.astype(str),errors='coerce')
#coerce is used to ignore the error
songs_66.dtype

#dealing with none
#The .fillna method will replace them with given values
songs_66.fillna(-1)

#NaN values can be dropped from the series using
#.dropna
songs_66.dropna()

####################################
#Append ,combining and joining two series
songs_69=pd.Series([7,16,21,39],index=['A','B','C','D'],name='counts')
#to oncatenate two series together,simply use .append
songs=songs_66.append(songs_69)
songs



##################################
#plotting series

import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot()
plt.legend()
#select whole code block
##########
#Bar
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66 =pd.Series([3,12,11,9],index=['George','Ringo','John','Paul'],name='Counts')
songs_66.dtypes
songs_66.plot(kind='bar',color='r')
songs_66=pd.to_numeric(songs_66)
plt.legend()

################################
#Histogram
import numpy as np
data=pd.Series(np.random.randn(500),name='500 random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

###################################
#create using construtor
#create pandas dataframe from list
import pandas as pd
technologies=[["Spark",20000,"30days"],["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)


#################
column_names=["courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
##Check datatypes
df.dtypes

##############################################
#you can also assign custom
#data types to column
#set custom types to DataFrame

import pandas as pd
technologies={'Courses':["Spark","Pyspark","Pandas","Java"],
              'Fee':[20000,25000,22000,23000],
              'Duration':['30days','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,23.2]}
df=pd.DataFrame(technologies)
print(df.dtypes)

##convert all types to best possible types

df2=df.convert_dtypes()
print(df2.dtypes)

##change all columns to same type
df=df.astype(str)
print(df.dtypes)

##change types for one or multiple columns
df= df.astype({"Fee":int,"discount":float})
print(df.dtypes)
print(df)

#convert data types for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','discount']
df[cols]=df[cols].astype('float')
df.dtypes

#Ignores error
df=df.astype({"Courses":int},errors='ignore')
df.dtypes
#Generate error
df=df.astype({"Courses":int},errors='raise')

df=df.astype(str)

#################################################
#create dataframe from dictionary
import pandas as pd
technologies={'Courses':["Spark","Pyspark","Pandas","Java"],'Fee':[20000,25000,22000,23000],'Duration':['30days','40days','20days','50days'],'discount':[11.8,12.3,45.6,23.2]}
df=pd.DataFrame(technologies)
df

#convert dataframe to csv
df.to_csv('data_file.csv')

#########
#create DataFrame from CSV file
df=pd.read_csv('data_file.csv')

