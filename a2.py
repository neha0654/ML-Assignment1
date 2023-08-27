import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
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
X = df.drop(['Customer', 'Payment (Rs)', 'Label'], axis=1)
y = df['Label']
x_train, xtest, y_train, ytest = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
x_scale = scaler.fit_transform(x_train)
xtest_scale = scaler.transform(xtest)
model1 = RandomForestClassifier(random_state=42)
model1.fit(x_scale, y_train)
ypred = model1.predict(xtest_scale)
print(classification_report(ytest, ypred))