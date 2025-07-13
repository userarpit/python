import pandas as pd
df = pd.read_csv('nba.csv')
print(df)
print(len(df))
df.dropna(inplace=True)
print(len(df))