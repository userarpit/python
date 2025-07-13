import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head())
print("*******" * 10)
print(df.iloc[0:2,0:5])