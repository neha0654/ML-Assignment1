import pandas as pd
import numpy as np

df=pd.read_excel("Lab Session1 Data.xlsx", sheet_name="Purchase data")
df=df.iloc[0:10,0:5]
m=np.array(df['Payment (Rs)'])
n=len(m)
label=[]
c=0
for i in range(0,n):
    c=c+1
    if m[i]>200:
        label.append('Rich')
    else:
        label.append('Poor')
df.insert(loc = 5,column = 'Label',value = label)
print(df)