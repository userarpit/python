import pandas as pd

df = pd.read_csv("practice/name_score.csv",header=None)
print(df.shape)

print(df[:2])
