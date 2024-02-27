import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("mtcars.csv")
d.describe()
a=d.describe()
#initialize the scaler
scaler=StandardScaler()
df=scaler.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()
#there if you will check res, in variable environment there

###############################################
