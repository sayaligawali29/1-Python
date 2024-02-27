# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:41:14 2023

@author: ACER
"""

#data dictionary
#index
#speed:the car running by speed
#dist:the distance covered

############################################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis
Q1_a= pd.read_csv("c:/2-Datasets/Q1_a.csv")
Q1_a.describe()
#finding shape
print(Q1_a.shape)
'''(50, 3)'''
###########################################################
#finding the columns
print(Q1_a.columns)
'''Index(['Index', 'speed', 'dist'], dtype='object')'''
###########################################################


##########################################################
#check missing value
print(Q1_a.isnull)
'''there is no missing value'''
############################################################
#print first and last 5 value from given dataset
Q1_a.head()
Q1_a.tail()
########################################################
#How many data points for each class are present?
Q1_a['speed'].value_counts()
#############################################################
#scatter plot
Q1_a.plot(kind='scatter',x='speed',y='dist');
plt.show()
#####################################################
#Histogram
sns.FacetGrid(Q1_a, hue="speed", height=5) \
    .map(sns.distplot, "dist") \
    .add_legend();
plt.show();

##########################################################
Q1_a.describe()
plt.hist(Q1_a.speed)
sns.distplot(Q1_a['speed'],kde=True,bins=6, density=True)
plt.hist(Q1_a.dist)
###########################################################

counts, bin_edges = np.histogram(Q1_a['speed'], bins=10, density = True)
pdf = counts/(sum(counts))
print(pdf);
'''[0.04 0.06 0.08 0.12 0.16 0.1  0.14 0.16 0.02 0.12]'''
##############################################################
print(bin_edges);
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf);
plt.plot(bin_edges[1:], cdf)

'''we can visually see  that what percentage of speed and distance
less than sum values
80% of cars speed is 20 km/hrs
60% of cars speed is 17.5 km/hrs
'''

#box 
sns.boxplot(Q1_a.speed)
#the mean speed of all cars was 25km
#the minimum speed was 5km and max was 
sns.boxplot(Q1_a.dist)
plt.show()
###########################################
#standerd deviation
print(np.std(Q1_a['speed']))
print(np.std(Q1_a['dist']))
###############################################
#median

#############################################
sp_lst=Q1_a['speed'].tolist()
sp_lst

print('skewness of speed',skew(sp_lst))
dist=Q1_a['dist'].tolist()
print('skewness of dist',skew(dist))
print(kurtosis(dist,axis=0,bias=True))
