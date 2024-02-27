# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
Q2=pd.read_csv('c:/1-Datasets/Q2_b.csv')


Q2.describe
Q2.shape
Q2.dtypes

Q2['SP'].value_counts()

Q2.plot(kind='scatter',x='SP',y='WT',color='g',title='ABC')  #we can cahnges graph here #scatter,pie,bar,hist, 
plt.show()

sns.FacetGrid(Q2, hue="SP", height=5) \
   .map(sns.distplot, "WT") \
   .add_legend();
plt.show();

#############################
counts, bin_edges = np.histogram(Q2['SP'], bins=10, density = True)
pdf = counts/(sum(counts))
pdf
###############################################################


################################################################