#write a pandas program to create a datafram from dictionary and 
#display it

import pandas as pd
d={'X':[78,85,96,80],'Y':[84,94,89,83],'Z':[86,97,96,90]}
df=pd.DataFrame(d);
print(df)

#write a pandas program to create a dataframe from specified
#Sample python dictionary data and list labels
#exam_data={'name':['Ram','Sham','Ghansham','Krishna'],'score':[12.5,6,45.6,np.nan],
#'attempts':[1,2,3,4],'Qualify':['yes','no','yes,'yes'],labels:['a','b','c','d]}
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data)
print(df)

#write a pandas program to display of the
#summery of basic information
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data)
print("Summery of information")
print(df.info())
df.describe()

###write pandas program to get first 3 rows of dataframe

import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data)
df1=df.iloc[:3]
print(df1)

#write a pandas program to select name and score column
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data)
print(df[["name","score"]])

#write a pandas program to select the specified columns and rows from the 
#dataframe
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data)
print(df[["score","Qualify"]])

#write pandas program to select to where number of attempts are
#greater than two

import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("Attempts in exam greater than 2")
print(df[df['attempts']>2])
#or
df2=df.loc[df.attempts>2]

##write pandas program to count the number 
#of rows and column 
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)

rows_count=len(df.axes[0])
print(rows_count)
column_count=len(df.axes[1])
print(column_count)

total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows:"+str(total_rows))
print("Number of Columns:"+str(total_cols))


'''write a pandas program to select the rows where the score is 
is missing ,i.e is NaN'''

import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("Rows where score is missing:")
df2=(df[df['score'].isnull])

''' write pandas program to select the rows the score
is between 15 and 20 '''

import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12.5,6,45.6,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("Rows where score between 15 and 20(inclusive):")
df2=df[df['score'].between(15,20)]
print(df2)

'''write pandas program to select the rows where number
of attempts int the exam is less than 2 and score greater than 15 '''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12,16,19,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("Number of attempts in the examinations is less than 2 greater than 15")
print(df[(df['attempts']<2) & (df['score']>15)])


''' write a search pandas program to change the score in rows
in 'd' to 11.5'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12,16,19,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("\n Change the score in row 'd' to 11.5")
df.loc['d','score']=11.5
print(df)
##########################################################
''' write a search pandas program to calculate the sum of
the examination attempts by the students'''

import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12,16,19,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print(df['attempts'].sum())


''' write a pandas program to calculate mean of all students score '''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12,16,19,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print(df['score'].mean())

df.describe()

''' write pandas program to append a new row 'k' to
dataframe with given values for each column'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12,16,19,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("ORIGINAL DATAFRAME")
df.loc['k']=['Suresh','20.5','2','yes']
print("print all  record")
print(df)

'''write pandas program to sort the dataframe first
by 'name' in descending order, then by 'score' in ascending
order '''

import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
           'score':[12,16,11,None],
           'attempts':[1,2,3,4],
           'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
print("Orignal rows:")
print(df)
df=df.sort_values(by=['name'],ascending=[False])
print(df)
df=df.sort_values(by=['score'],ascending=[True])
print(df)

'''write pandas program to replace qualify column contains
 yes or no with true or false'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
            'score':[12,16,11,None],
            'attempts':[1,2,3,4],
            'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
#map() use to map true or false or yes or no
df['Qualify']=df['Qualify'].map({'yes':True,'no':False})
print(df)

'''write pandas program to change the name 'Ram' to'Om'
name column of the DataFrame'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
            'score':[12,16,11,None],
            'attempts':[1,2,3,4],
            'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
df['name']=df['name'].replace('Ram','Om')
print(df)

###############################
''' write pandas program to insert a new column in existing
dataframe'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
            'score':[12,16,11,None],
            'attempts':[1,2,3,4],
            'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
color=['Red','Orange','Blue','Black']
df['color']=color
print(df)

'''write pandas program to iterate over rows 
in a dataframe '''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Krishna'],
            'score':[12,16,11,None],
            'attempts':[1,2,3,4],
            'Qualify':['yes','no','yes','yes']}
labels=['a','b','c','d']
df=pd.DataFrame(exam_data,index=labels)
df
for index,row in df.iterrows():
    print(row['name'],row['score'])
    
