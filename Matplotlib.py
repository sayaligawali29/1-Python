import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show


#########################################################
#Multiline plots
import matplotlib.pyplot as plt 
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3.0 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])
plt.show()

#########################################################
#note how matplotlib chooses different color automatically 

#grid,axes,and labels
#Adding a grid

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()

#########################################################
#Handling axes
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.axis()
plt.axis([0,5,-1,13])

plt.grid(True)
plt.show()

########################################################
#Adding  Labels
#.x&y label is used to give label to axes
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel('This is the Xlabel')
plt.ylabel('This is the Ylabel')
plt.show()

########################################################
#Adding titles
#.title() is used to give title to graph
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title("This is title")
plt.show()

########################################################
#Adding legend
#legend() used to provide information of graph on graph
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()

############################################################
'''color abrevetion
b blue
c cyan
g green
k black
m magenta
r red 
w white
y yellow'''


#control colors
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

######################################################
#specifying styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':')
plt.show()

######################################################
'''style abrevations style
solid line
dotted line
dash line
dash dot line
'''

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()

####################################################
#Histogram Chart
#.hist() used to plot histogram
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y)
plt.show()

#####################################################
#Bar plot
#bar plot to understand the trend of the data
#EDA exploratory data analysis

import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5])
plt.show()


#####################################################
#Scatter plots
'''scatter plot display vslues of two sets of data the data 
visualization is done as a collection of points connected to lines
each of them has its cooridnates determine by the value
of the variable (one varibale determines the x position the 
                 other the y positin)'''

#to find colinearity

import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

############
size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors)
plt.show()

#######################################################
#Adding text
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(-4,4,1024)
Y=.25*(X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(X,Y,c='k')
plt.show()

#########################################################
