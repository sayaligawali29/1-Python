###################JOINS########################
import pandas as pd
technologies={"Courses":["Spark","Pyspark","Python","Pandas"],
              "Fee":[20000,25000,22000,39000],
              "Duration":['30days','40days','35days','50days']}
index_labels=['r1','r2','r3','r4']

df1=pd.DataFrame(technologies,index=index_labels)

technologies1={"Courses":["Spark","Java","Python","Go"],
               "Discount":[2000,2300,1200,2000]}

index_label1=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies1,index=index_label1)

#pandas inner join is mostly used join
#It is used to join two dataframes on indexes
#when indexes dont match the rows get dropped from both dataframe

##########################################
#pandas join ,by default it will join the table left join

df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

##INNER JOIN##
#pandas inner join dataframe
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

##LEFT JOIN##
df3=df1.join(df2,lsuffix="_left", rsuffix="_right",how="left")
print(df3)

##RIGHT JOIN##
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="right")
print(df3)

##Pandas join on column
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df3)

df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='left')
print(df3)

df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='right')
print(df3)

#Pandas Merge DataFrame
import pandas as pd
technologies={"Courses":["Spark","Pyspark","Python","Pandas"],
              "Fee":[20000,25000,22000,39000],
              "Duration":['30days','40days','35days','50days']}
index_labels=['r1','r2','r3','r4']

df1=pd.DataFrame(technologies,index=index_labels)

technologies1={"Courses":["Spark","Java","Python","Go"],
               "Discount":[2000,2300,1200,2000]}

index_label1=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies1,index=index_label1)

#using pandas .merge()
df3=pd.merge(df1,df2)
df3

#using dataframe .merge()
df3=df1.merge(df2)


##Use pandas.concat() to concat two dataframe
import pandas as pd
df=pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                 'Fee':[20000,25000,22000,30000]})

df1=pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})

#using pandas .concat() to concat two dataframes
data=[df,df1]
df2=pd.concat(data)
df2

##Concatenate multiple dataframe using pandas.concat()
import pandas as pd
df=pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                 'Fee':['20000','25000','22000','30000']})

df1=pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
                  'Fee':['25000','25200','24500','24900']})

df2=pd.DataFrame({'Duration':['30days','40days','35days','60days','55days'],
                  'Discount':[1000,2300,2500,2000,3000]})

#appending multiple dataframe
df3=pd.concat([df,df1,df2])
print(df3)

#Write Dataframe to csv file with default params
