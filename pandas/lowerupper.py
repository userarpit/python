import pandas as pd

df = pd.read_csv("nba.csv",nrows=5)
df1 = pd.read_csv("nba.csv",nrows=5,skiprows=[1,4])



# df['Name'] = df['Name'].str.lower()
df['College'] = df['College'].str.swapcase().str.title()
print(df)
print("****")
print(df1)
