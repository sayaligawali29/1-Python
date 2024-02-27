import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("Boston.csv")
df.describe
df.shape
df.columns
df.dtypes
df.rad=df.rad.astype(int)
df.dtypes

#2-D Scatter plot
df.plot(kind='scatter',x='crim',y='zn',color='g');
plt.show()

#pair-plot
sns.set_style("whitegrid")
sns.pairplot(df,hue="zn",height=3)
plt.show()

#
