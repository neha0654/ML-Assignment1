import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel("Lab Session1 Data.xlsx", sheet_name="IRCTC Stock Price")
cD=df.iloc[:,3:4]
meanD=np.mean(np.array(cD))
variance_D=np.var(np.array(cD))
data_wed=df.loc[df['Day']=='Wed']
datawedprice=data_wed.iloc[:,3:4]
meanwed=np.mean(np.array(datawedprice))
dataapr=df.loc[df['Month']=='Apr']
dataapr_price=dataapr.iloc[:,3:4]
meanApr=np.mean(np.array(dataapr_price))
dataChg=df.iloc[:,8:9]
data_chg_array=np.array(dataChg)
data_chg_wed=np.array(data_wed.iloc[:,8:9])
n=len(data_chg_array)
neg_count=0
for i in range(0,n):
    if data_chg_array[i]<0:
        neg_count=neg_count+1
loss_prob=neg_count/n
wed_count=0
n1=len(data_chg_wed)
for i in range(0,n1):
    if data_chg_wed[i]<0:
        wed_count=wed_count+1
profit_wed=wed_count/n1
weddata = df[df['Day'] == 'Wed']
wedprofit = np.mean(weddata['Chg%'] > 0)
wedprob = np.mean(df['Day'] == 'Wed')
cdprob = (wedprofit / wedprob)
print('Mean is  :', meanD)
print("Variance is : ",variance_D)
print('Mean on wednesday is  :',meanwed )
print('Mean in april i :', meanApr)
print("Probability of loss is  : ",loss_prob)
print("Probability of profit on wednesday is  : ",profit_wed)
print('Conditional Probability on Wednesday is:', cdprob)
plt.scatter(df['Day'], df['Chg%'])
plt.xlabel('Day')
plt.ylabel('Chg%')
plt.title('Chg% vs Day')
plt.show()
