
import pandas as pd
df=pd.read_csv("c:/2-Datasets/ethnic diversity.csv")
#to check column type
df.dtypes
#salaries data type is float,let us convert into int
df.Salaries=df.Salaries.astype(int)
df.dtypes
#the datatype of salaries is int
#similarly age data type must be float
df.age=df.age.astype(float)
df.dtypes
df.shape
print(df.columns)

####################################################
#identify the duplicates
df_new=pd.read_csv("education.csv")
duplicate=df_new.duplicated()
#output of this fuction is single column
#if there is duplicate records output-True
#if there is no duplicate records output-false
#series will be created
duplicate
sum(duplicate)
#output will be 0


##################################################
df_new1=pd.read_csv("mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)

##################################################
import pandas as pd
import seaborn as sns
df=pd.read_csv("ethnic diversity.csv")
#Now let us find outlier in Salaries
sns.boxplot(df.Salaries)
sns.boxplot(df.age)
#there is no outlier
#let us calculate IQR
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observe IQR in variable explorer
#no,because IQRvis in capital letters treated as constant
IQR
#but if we will try as I,Iqr or iqr then it is showing 
lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
upper_limit=df.Salaries.quantile(0.75)+1.5*IQR



#######################################################
#TRIMMING

import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit,True,False))
#you can check outlier_df column in variable explorer
df_trimmed=df.loc[~outliers_df]
df.shape
df_trimmed.shape

#######################################################
#Replacement Techniques
#Drawback of trimming technique is we are losing the data
df=pd.read_csv("ethnic diversity.csv")
df.describe()
#record no 23 has got outliers
#map all the outlier values to upper limit

df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if the values are greater than upper_limit
#map it toupper limit

#####################################################
#Winsorizer
import seaborn as sns
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method ='iqr',
                  tail='both',
                  fold=1.5,
                  variables=['Salaries'])

#copy winsorizer and paste in help tab of
#top right window,study the method

df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])

#####################################
#Zero variance and near zero variance
#if there is no variance in the feature,then ML model
#will not get any intellignence,so it is better to 
#igonre features

import pandas as pd
df=pd.read_csv("ethnic diversity.csv")
df.var()
#here Empid and zip is nominal data
#salary has 4.441953e+08 which is not close  to 0
#similarly age 8.571358e+01=85.71
#both the features are having considerable variance
df.var()==0
#output
'''
EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool
'''
#None of them are equal to zero
df.var(axis=0)==0
df.var(axis=1)==0
'''
EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool
'''
######################################################
import pandas as pd
import numpy as np
df=pd.read_csv("modified ethnic.csv")
#to check null value
df.isna().sum()
'''
Position            43
State               35
Sex                 34
MaritalDesc         29
CitizenDesc         27
EmploymentStatus    32
Department          18
Salaries            32
age                 35
Race                25
'''

######################################################
#create an imputer that create NaN value
#mean and median is used for nummeric data
#mode is used for discrete data pos,sex,maritalDes
from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
#check the dataframe
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
#check the dataframe
df['Salaries'].isna().sum()

###################################################
import pandas as pd
import seaborn as sns
data = pd.read_csv("ethnic diversity.csv")
data.head(10)
data.info()

#It gives size,null value 

data.describe()
data['Salaries_new']=pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.mean(),max(data.Salaries)],labels=['Low','High'])

data.Salaries_new.value_counts()

data['Salaries_new'] = pd.cut(data['Salaries'],bins=[min(data.Salaries),data.Salaries.quantile(0.25),data.Salaries.mean(),data.Salaries.quantile(0.75),max(data.Salaries)],labels=['group1','group2','group3','group4'])
data.Salaries_new.value_counts()

#############################################
import pandas as pd
import numpy as np
df=pd.read_csv('animal_category.csv')
df
df.shape
df.drop(['Index'],axis=1,inplace=True)

df_new=pd.get_dummies(df)
df_new.shape

df_new.drop(['Gender_Male','Homly_Yes'],axis=1,inplace=True)
df_new.shape

df_new.rename(columns={'Gender_Female':'Gender','Homly_No':'Homly'},inplace=True)
df_new.shape

#####################################
import pandas as pd 
import numpy as np
df=pd.read_csv("ethnic diversity.csv")
df
df.shape
df.drop(['EmpID'],axis=1,inplace=True)
df_new=pd.get_dummies(df)
df_new.shape

###################################################
#one hot encoder
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
df=pd.read_csv("ethnic diversity.csv")
df.columns
#we have salaries and age as numerical column,let us make them 
#at position 0 and 1 so to make further data processing easy

df=df[['Salaries','age','Position',
       'State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Department','Race']]
#check the dataframe in variable explorer
#we want only nominal data and ordinal data for processing
#hence skipped 0th the first column and applied to one encode
enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]).toarray())

#################################################
#Label Encoder
from sklearn.preprocessing import LabelEncoder
#creating instance of label encoder
labelencoder=LabelEncoder()
#split your data into input and output variables
X=df.iloc[:,0:9]  #first 8 columns for X and 9th for y or 
y=df['Race']
df.columns
#we have nominal data Sex,MartialDesc,CitizenDesc
#we want to convert to label encoder
X['Sex']=labelencoder.fit_transform(X['Sex'])
X['MaritalDesc']=labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc']=labelencoder.fit_transform(X['CitizenDesc'])

#label encoder y

y=labelencoder.fit_transform(y)
#This is going to create an array,hence convert it back
#to dataframe
y=pd.DataFrame(y)
df_new=pd.concat([X,y],axis=1)
#if you will see variable explorer,y do not have column name
#hence rename the column
df_new=df_new.rename(columns={0:'Race'})

######################################################
ethnic=pd.read_csv("ethnic diversity.csv")
#now read the columns
ethnic.columns
#there are some columns which not 
ethnic.drop('')
a1=ethnic.describe()
#check all data frame in variable explorer
#you find minimum salary is 0 and max is 108304
#same way check for age and their huge difference
#in min and max value hence we are going for normalization
#first we will have to convert non numeric data


ethnic=pd.get_dummies(ethnic,drop_first=True)
def norm_func(i):
    x=(i-i.min()/(i.max()-i.min()))
    return x
df_norm=norm_func(ethnic)
b=df_norm.describe()
#if you will observe the b frame
#it has dimension 8,81
#earlier in they were 8,11,it is beacause all non numberic
#data has been converted to numeric using label encoding

