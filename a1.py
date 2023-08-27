import pandas as pd
import numpy as np
df=pd.read_excel("Lab Session1 Data.xlsx", sheet_name="Purchase data")
df=df.iloc[0:10,0:5]
df1=df.iloc[0:10,1:5]
A=np.array(df.iloc[0:10,1:4])
C=np.array(df.iloc[0:10,4:5])
Ainv=np.linalg.pinv(A)
X=np.matmul(Ainv,C)
rank = np.linalg.matrix_rank(np.array(df1))
rank_a_mat=np.linalg.matrix_rank(A)
print("Dimentionality : ",rank)
print("Rank A : ",rank_a_mat)
print("Cost of each procuct : ")
print(X)