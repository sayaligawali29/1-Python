# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:28:50 2023

@author: user
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis
cars = pd.read_csv('c:/2-dataset/Cars.csv')
cars.columns
cars.describe()
cars.shape
cars.dtypes
cars.plot(kind='scatter',x='SP',y='WT',color='g',title='ABC')  #we can cahnges graph here #scatter,pie,bar,hist, 
plt.show()

sns.FacetGrid(cars, hue="SP", height=5) \
   .map(sns.distplot, "WT") \
   .add_legend();
plt.show();

###################
counts, bin_edges = np.histogram(cars['SP'], bins=10, density = True)
pdf = counts/(sum(counts))
pdf