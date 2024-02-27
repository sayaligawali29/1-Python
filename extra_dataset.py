import pandas as pd
import numpy as np
df=pd.read_csv('c:/2-Datasets/loan.csv')
df.dtypes
df.size
df['id']
df[['id','term']]
df2=df[1:5]
df2

#convert all types to best possible types

df2=df.convert_dtypes()
print(df2.dtypes)

#change all colums to same datatypes
df=df.astype(str)
print(df.dtypes)

##change types for one or multiple columns
df=df.astype({"id":int,"funded_amnt":float})
print(df.dtypes)

#convert data types for all columns in a list
cols=['id','member_id']
df[cols]=df[cols].astype('float')
df.dtypes

#Ignores error
df=df.astype({"member_id":int},errors='ignore')
df.dtypes

#Generate error
df=df.astype({"id":float},errors='raise')
df.dtypes

## Substracting specific values from a cloumn
df['funded_amnt']=df['funded_amnt']-500
df['funded_amnt']

#it will show 5 number summery
df.describe()

###rename()
##rename the specific column 
df.rename(columns = {"id": "id's"},  inplace = True)
df


df2=df.iloc[2] #select row by index
df2
df2=df.iloc[[2,3,6]]#select rows by index list
df2=df.iloc[1:5] # select rows by integer index range
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]# select first 3 rows
df2=df.iloc[-1:]# select last row
df2=df.iloc[-3:]# select last 3 rows
df2=df.iloc[::2]# select alternate rows

#Select rows by index labels
df2=df.loc[2] # select row by label
df2=df.loc[[0,3,6]] #select rows by index 
df2=df.loc[0:5]  # slect rows by label index
df2=df.loc[1:7:4]#select alternate rows 



#######################################################
########################################################
#########################################################
import pandas as pd
import numpy as np
df=pd.read_csv('c:/2-Datasets/crime_data.csv')
df
df.dtypes
df.size
#accessing single column
df['Murder']

df[['Rape','Assault']]
df

#convert all types to best possible types

df2=df.convert_dtypes()
print(df2.dtypes)

###change types for one or multiple columns
df=df.astype({"Murder":int,"UrbanPop":float})
print(df.dtypes)

#convert data types for all columns in a list
cols=['Rape','UrbanPop']
df[cols]=df[cols].astype('int')
df.dtypes

#Ignores error
df=df.astype({"Murder":int},errors='ignore')
df.dtypes

#Generate error
df=df.astype({"Murder":int},errors='raise')
df.dtypes

## Substracting specific values from a cloumn
df['Rape']=df['Rape']-5
df['Rape']

#it will show 5 number summery
df.describe()

###rename()
##rename the specific column 
df.rename(columns = {"Rape": "Rapiest"},  inplace = True)
df
#renaming multiple columns
df.rename({"Murder": "Murder's", 
           "Assault": "Assault's", 
           "Rape": "Rapiest"}, 
          axis = "columns", inplace = True)


df2=df.iloc[2] #select row by index
df2
df2=df.iloc[[2,3,6]]#select rows by index list
df2=df.iloc[1:5] # select rows by integer index range
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]# select first 3 rows
df2=df.iloc[-1:]# select last row
df2=df.iloc[-3:]# select last 3 rows
df2=df.iloc[::2]# select alternate rows

#Select rows by index labels
df2=df.loc[2] # select row by label
df2=df.loc[[0,3,6]] #select rows by index 
df2=df.loc[0:5]  # slect rows by label index
df2=df.loc[1:7:4]#select alternate rows 


#########################################################
#########################################################
#########################################################
import pandas as pd
import numpy as np
df=pd.read_csv('c:/2-Datasets/bank_data.csv')
df

df.dtypes
df.size
df['age']
df[['age','balance']]
#convert all types to best possible types

df2=df.convert_dtypes()
print(df2.dtypes)

###change types for one or multiple columns
df=df.astype({"age":float,"loan":float})
print(df.dtypes)

#convert data types for all columns in a list
cols=['age','balance']
df[cols]=df[cols].astype('int')
df.dtypes

## Substracting specific values from a cloumn
df['age']=df['age']-5
df['age']

#it shows 5 number summery
df.describe

#rename() specific column 
df.rename(columns = {"loan": "loan_bal"},  inplace = True)
df
#renaming multiple columns
df.rename({"age": "ages", 
           "balance": "balance's", 
           "pdays": "paydays"}, 
          axis = "columns", inplace = True)
df
df.info

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

#Select rows by index labels
df2=df.loc[2] # select row by label
df2=df.loc[[0,3,6]] #select rows by index 
df2=df.loc[0:5]  # slect rows by label index
df2=df.loc[1:7:4]#select alternate rows 

