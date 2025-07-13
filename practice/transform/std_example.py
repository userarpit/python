import pandas as pd
import numpy as np

data = {
    "A": [10, 12, 11, 13, 14],
    "B": [5, 10, np.nan, 20, 25],  # Has a NaN
    "C": [100, 101, 100, 102, 101],
    "D": ["cat", "dog", "mouse", "fish", "bird"],
}  # Non-numeric
df = pd.DataFrame(data)

print(df)
print(f"{df['B'].std(skipna=False):.2f}")
print(df.describe())
# print(df.std())
df_new = df.drop(columns=['D'])
print(df_new.std())
print(df_new.var())

print(df_new.std(axis=1))

print("-" * 30)

data_small = pd.Series([10, 20, 30])
std_sample = data_small.std(ddof=1)  # Sample standard deviation
print(f"Sample standard deviation of small data: {std_sample:.2f}")

data_small = pd.Series([10, 20, 30])
std_sample = data_small.std(ddof=0)  # Sample standard deviation
print(f"Population standard deviation of small data: {std_sample:.2f}")

print(df.std(numeric_only=True))