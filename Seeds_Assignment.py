import pandas as pd
import numpy as np
df5=pd.read_csv('c:/1-Python/Seeds_data.csv')
df5
##pandas.Dataframe.query() by examples
#query all rows with area==14.11
df2=df5.query("Area==14.11")
print(df2)

df2=df5.query("Area!=14.11")
print(df2)

#Adding columns to dataframe
rows=df5.shape[0]
for i in range(rows):
    df2['rating']=1
    df2['price']=250
df2

#Slicing specific rows and column using iloc
df3=df5.iloc[1:2,1:3]
df3
#Select rows by integer index
#select row by index
df2=df5.iloc[2] 
df2
#select rows by index list
df2=df5.iloc[[2,3,6]]
 # select rows by integer index range
df2=df5.iloc[1:5]
#select first row
df2=df5.iloc[:1]
# select first 3 rows
df2=df5.iloc[:3]
# select last row
df2=df5.iloc[-1:]
# select last 3 rows
df2=df5.iloc[-3:]
# select alternate rows
df2=df5.iloc[::2]

#Select rows by index labels
# select row by label
df2=df5.loc[0]
 #select rows by index  
df2=df5.loc[[0,1,2,3]]
# slect rows by label index
df2=df5.loc[3:9]
#select alternate rows   
df2=df5.loc[10:50:2]

#derive new column from existing column
df2=df5.assign(Area=lambda x:x.length * x.Area/100)
print(df2)

#########################################################
#seelct multiple columns
df2=df5.loc[:,["Area","length","Width"]]
#select random columns
df2=df5.loc[:,["Area","length","Width"]]
#select columns between two columnd
df2=df5.loc[:,'length':]
#############################
# pandas program display of the summery of basic information
df5.describe()
print(df5)

# pandas program to get first 3 rows of dataframe
df3=df5.iloc[:3]
print(df3)

# pandas program to select Area and length column
df4=df5[['Area','length']]

# pandas program to select where area is greater than 14.11
df6=(df5[df5['Area']>15.26])
print(df6)

#pandas program to count the number of rows and column 
rows_count=len(df5.axes[0])
print(rows_count)
column_count=len(df5.axes[1])
print(column_count)

#pandas program to check whether the value is none
d=([df5['Area'].isnull])
print(d)

#pandas program to select the rows the score
#is between 15 and 20
df6=df5[df5['Area'].between(15,20)] 
print(df6)

#pandas program to select the rows where number
#of attempts int the length is less than 14 and area greater than 15 '''
df7=(df5[(df5['length']<6) & (df5['Area']>15)])

print(df7)

#pandas program to change the Area in rows
#index 0 to 11.5
df5.loc[0,'Area']=19.6
print(df5)

# pandas program to calculate the sum of
#the examination attempts by the students
print(df5['Area'].sum())

#pandas program to calculate mean of length
print(df5['length'].mean())

#pandas program to iterate over rows in a dataframe
for index,row in df5.iterrows():
    print(row['Area'],row['Width'])
    
#pandas program to print area in ascending and descending order
df3=df5.sort_values(by=['Area'],ascending=[False])
print(df3)

df4=df5.sort_values(by=['Area'],ascending=[True])
print(df4)

#mapping
df5['Type']=df5['Type'].map({3:True,2:False})
df5
#############################################
#replace
df5['Area']=df5['Area'].replace(20.97,2)
df5

#write python program to read entire text file
import pandas as pd
df=pd.read_txt('programming.txt')
