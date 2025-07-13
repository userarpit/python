import pandas as pd
import numpy as np

data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Heidi",
        "Ivan",
        "Judy",
    ],
    "Age": [25, 30, 22, 35, 28, 40, 29, 31, 26, 33],
    "City": [
        "New York",
        "London",
        "Paris",
        "New York",
        "London",
        "Berlin",
        "Paris",
        "London",
        "New York",
        "Berlin",
    ],
    "Salary": [50000, 60000, 45000, 75000, 55000, 80000, 52000, 62000, 48000, 70000],
}
df = pd.DataFrame(data)

print(df)

sample_df = df.sample(frac=0.750, random_state=42, replace=True, ignore_index=True)
print(sample_df)

df["Salary weight"] = df["Salary"] / df["Salary"].max()
print(df)

df_sample = df.sample(
    n=5, random_state=42, replace=True, ignore_index=True, weights=df["Salary weight"]
)
print(df_sample)
print("*" * 100)
df_columns = df.sample(frac=0.80, axis=1)
print(df_columns)
