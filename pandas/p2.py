import numpy as np
import pandas as pd


df_index = pd.date_range("1/1/2000",periods=10)
df = pd.DataFrame(np.random.randint(1,100,(10,2)),index=df_index,columns=["A","B"])


a = np.random.randn(1000)
# print(np.random.randn(8, 3))
s = pd.Series(a)
print(s.head())
print(s.tail())

print(df)
df.columns = [x.lower() for x in df.columns]
print(df)
print(df.index.array)
df['c'] = df['a'].rdiv(df['b'])
print(df)
print(np.arange(10))
div,rem = divmod(pd.Series(np.arange(10)),2)
print(div)
print(rem)
