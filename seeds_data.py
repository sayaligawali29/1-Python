
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("Seeds_data.csv")
d.describe()
a=d.describe()
#initialize the scalar
scaler=StandardScaler()
df=scaler.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()