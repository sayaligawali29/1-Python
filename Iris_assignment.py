import pandas as pd
import numpy as np
df=pd.read_csv('c:/2-Datasets/Iris.csv')
df
##pandas.Dataframe.query() by examples
#query all rows with area==14.11
df2=df.query("SepalWidthCm==3.5")
print(df2)

df2=df.query("SepalWidthCm!=3.5")
print(df2)
#Adding columns to dataframe
rows=df.shape[0]
for i in range(rows):
    df2['rating']=1
    df2['price']=250
df2

#Slicing specific rows and column using iloc
df3=df.iloc[1:2,1:3]
df3
#Select rows by integer index
#select row by index
df2=df.iloc[2] 
df2
#select rows by index list
df2=df.iloc[[2,3,6]]
 # select rows by integer index range
df2=df.iloc[1:5]
#select first row
df2=df.iloc[:1]
# select first 3 rows
df2=df.iloc[:3]
# select last row
df2=df.iloc[-1:]
# select last 3 rows
df2=df.iloc[-3:]
# select alternate rows
df2=df.iloc[::2]

#Select rows by index labels
# select row by label
df2=df.loc[0]
 #select rows by index  
df2=df.loc[[0,1,2,3]]
# slect rows by label index
df2=df.loc[3:9]
#select alternate rows   
df2=df.loc[10:50:2]

#derive new column from existing column
df2=df.assign(SepalWidthCm=lambda x:x.PetalLengthCm * x.SepalWidthCm/100)
print(df2)

#seelct multiple columns
df2=df.loc[:,["SepalWidthCm","PetalLengthCm","Species"]]
#select random columns
df2=df.loc[:,["SepalWidthCm","PetalLengthCm","Species"]]
#select columns between two column
df2=df.loc[:,'SepalLengthCm':]

##Display the summery
df.describe()
df.info()

#pandas program to get first 3 rows of dataframe
df2=df.iloc[:3]
df2
# pandas program to select SepalWidthCm and PetalLengthCm column
df3=df[["SepalWidthCm","PetalLengthCm"]]
df3

#pandas program to select where SepalLengthCm is greater than 4.5
df6=(df[df['SepalLengthCm']>4.5])
df6

##pandas program to count the number of rows and column 
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
print(column_count)

#pandas program to check whether the value is none
d=([df['SepalLengthCm'].isnull])
print(d)

#pandas program to select the rows the score
#is between 4 and 5
df6=df[df['SepalLengthCm'].between(4,5)] 
print(df6)

#pandas program to select the rows where number
#of attempts in the PetalLengthCm is less than  an1.4 PetalWidthCm  greater than 3 '''
df7=(df[(df['PetalLengthCm']<1.4) & (df['PetalWidthCm']>3)])

#################################################
##############################################

def add_1000(x):
    return x+1000
df3 = ((df.Id).apply(add_1000))
df3

############################################################

def add_4(x):
    return x+4
df["PetalWidthCm"] = df["PetalWidthCm"].apply(add_4)



#Apply to multiple columns
def add_10(x):
    return x+10
df[['SepalLengthCm','SepalWidthCm']] = df[['SepalLengthCm','SepalWidthCm']].apply(add_10)


###################

#using lambda
#apply lambda function to specific column
df[['SepalLengthCm','SepalWidthCm']] =df[['SepalLengthCm','SepalWidthCm']].apply(lambda x:x+50)

################

#Using DataFrame.apply() & [] operator
import numpy as np
df['PetalWidthCm'] = df['PetalWidthCm'].apply(np.square)
df



#Using DataFrame.apply() & [] operator
import numpy as np
df['PetalLengthCm'] = np.square(df['PetalLengthCm'])
df


############################################
#Pandas groupby() with Examples
#      ===============   #


# for 1 column
df2 = df.groupby(['PetalWidthCm']).sum()
# for multiple
df3 = df.groupby(['SepalLengthCm','SepalWidthCm']).sum()

df3 = df.groupby(['SepalLengthCm','SepalWidthCm']).sum().reset_index()

######


col_head = list(df.columns.values)
print(col_head)

#####################################################
#Pandas Shuffle DataFrame Rows
df4 = df.sample(frac=1)
df4
df5 = df.sample(frac=0.5)
df5
df4 = df.sample(frac=1).reset_index(drop=True)
df4
df5 = df.sample(frac=0.5).reset_index(drop=True)
df5
###########################################