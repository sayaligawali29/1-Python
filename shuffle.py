
#Pandas Dataframe shuffled rows
import pandas as pd

technologies={'Courses':["Spark","Pyspark",None,"Pandas","Java"],
              'Fee':[20000,25000,None,22000,23000],
              'Duration':['30days','','40days','20days','50days'],
              'discount':[11.8,12.3,45.6,11.5,23.2]}

df=pd.DataFrame(technologies)
print(df)

#frac=1 means 100% shuffling of rows
#frac=0.5 means 50% shuffling of rows
df1=df.sample(frac=1)
df1=df.sample(frac=0.5)
print(df1)

#######################################################
#create a new index starting from 0
df2=df.sample(frac=1).reset_index()
print(df2)

########################################################
#Drop Shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
df1


########################################################