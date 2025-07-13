import math
import pandas as pd
from statistics import mode

df1 = pd.read_csv("Xtra-Mart1.csv")
df2 = pd.read_csv("Xtra-Mart2.csv")

# df_com = pd.merge(df1,df2,on='CustID',how='left')
# print(df_com)

# df_com = pd.merge(df1,df2,on='CustID',how='right')
# print(df_com)

# df_com = pd.merge(df1,df2,on='CustID',how='inner')
# print(df_com)

df_com = pd.merge(df1,df2,on='CustID',how='outer')
print(df_com)

df_com['Customer Age'].fillna(math.floor(df_com['Customer Age'].mean()),inplace=True)
df_com['Gender'].fillna(mode(df_com['Gender']),inplace=True)
df_com.at[14,'City'] = 'Mumbai'
df_com.at[14,'Store Number'] = 10.0
df_com.at[14,'Sales (INR)'] = math.floor(df_com['Sales (INR)'].mean())
print(df_com)
