####################################################
#How to use Seaborn for data visualization
#pip install seaborn
#################SEABORN############################
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#seaborn has 18 in built datasets
#that can be found using the following
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()
#########################################################
#Count plot
'''A count plot is helpful when dealing with categorical
values .it is used to plot the frequency of the different
categories.the column sex contain categorical data in the tatanic
data,i.e male and female

'''
sns.countplot(x='sex',data=df)
#x-the name of the column
#data-the dataframe
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')
#hue the name categorical column to split the bars
#palette is used to change the set of color

##########################################################
#KDE plot
#kernal density estimate(KDE) plot is used to plot
#the distribution of continuous data

sns.kdeplot(x='age',data=df,color='black')


#x=the name of column
#data-the dataframe
#color-the color of the graph.you can find a list of column

#######################
#Distribution plot
sns.displot(x='age',kde=True,bins=6,data=df)
#kde=it is set to false by default .however,if you wish
#bin=the numbers of bars/bins
#the lower the number wider the bars and wider and the interval

sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)

######################################################
#first we will need to load iris dataset
df=sns.load_dataset('iris')
df.head
#scatter plot using seaborn

#Scatter plot help understand co relation between data,
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

######################################################
#Joint plot
# a joint plot is also used to plot corelation between the data
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')


########################################
#Pair plot
sns.pairplot(df)

##########################################
#a heat map can be used to visualize comnfusion ,matrices 
#and corelations
corr=df.corr()
sns.heatmap(corr)
