import numpy as np
import pandas as pd

df = pd.read_csv('employees.csv')
print(pd.isnull(df))
print(df[pd.isnull(df["Gender"])])
print("*************************" * 10)
print(df.notnull())
print("*************************" * 10)
print(df[pd.notnull(df["Gender"])])
print(pd.isnull(df).sum())
print(pd.isnull(df).sum().sum())

print("**************")
print(df.fillna(method ='pad'))
print(df.fillna(method ='bfill'))

df["Gender"].fillna("No Gender", inplace = True)  
print(df)
