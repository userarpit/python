import pandas as pd
df = pd.read_csv("Sales Data.csv")

print(df.head())
# print(df['Sales'])
print(df.groupby("Product")['Sales'].sum())
