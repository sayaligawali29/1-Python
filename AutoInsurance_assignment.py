# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:17:54 2023

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
ins=pd.read_csv('c:/2-datasets/AutoInsurance.csv')
a=ins.describe()
ins.dtypes
ins1=ins.drop(['Customer','State','Effective To Date'],axis=1)
ins_new=pd.get_dummies(ins1)
ins.shape #original dataframe contain 24 columns
ins1.shape # after dropping un wanted column we get 21 columns
ins_new.shape 
ins_new.dtypes
#creating dummy variable
#after that we get 60 columns

#checking columns of ins_new dataframe
ins_new.columns
#Now we have Gender ,response columns having only two possible 
#values so we need to drop one column and make only one column 
#after dummy variable
#as we know if we have n values for each columns then after creating dummy variables
#we should have n-1 columns.

#droping that extra columns
ins_new.drop(['Response_No','Coverage_Basic','Education_Bachelor','EmploymentStatus_Disabled','Gender_F','Location Code_Rural','Marital Status_Divorced','Policy Type_Corporate Auto','Renew Offer Type_Offer4','Sales Channel_Agent','Vehicle Class_Luxury Car'],axis=1,inplace=True)
ins_new.columns

#renaming columns
ins_new.rename(columns={'Response_Yes':'Response_No','Gender_M':'Gender'})

#5 number summery
des=ins_new.describe()

#normalizing data
#between 0 to 1
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

ins_norm=norm_fun(ins_new.iloc[:,:])
d=ins_norm.describe()


#Clustering
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or agglomerative clustering
#ref the help for linkage
b=linkage(ins_norm,method='complete',metric='euclidean')
plt.figure(figsize=(20,17))
plt.title('Hierarchical clustering dendrogram')
sch.dendrogram(b,leaf_rotation=0,leaf_font_size=10)
plt.show()


#using agglomerative clustering
from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean').fit(ins_norm)
#apply labels to the clusters
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#Assign this series to univ dataframe as column and name the column as 'clust'
ins_norm['clust']=cluster_labels
res=ins_norm.groupby(ins_norm.clust).mean()

#copying dataframe to insurance file
ins_norm.to_csv("Insurance.csv",encoding='utf-8')
import os
os.getcwd()
