import pandas as pd

df = pd.read_csv('car.csv')
print(df.head())

print(df.groupby('Location')['Location'].count())