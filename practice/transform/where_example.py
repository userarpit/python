import pandas as pd
import numpy as np

data = {"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50], "C": [100, 150, 200, 250, 300]}

df = pd.DataFrame(data)
print(df)


# print(df['A'])
df_where_A = df.where(df["A"] >= 3, other=0)
print(df_where_A)


# print(type(df >= 20))
df_where_all_less_20 = df.where(df >= 20, other=0)
print(df_where_all_less_20)


df_multi_cond = df.where((df["A"] >= 3) & (df["B"] <= 40), other=-1)
print(df_multi_cond)


replacement_df = pd.DataFrame(
    {"A": [100, 200, 300, 400, 500], "B": [5, 6, 7, 8, 9], "C": [0, 0, 0, 0, 0]}
)

df.where((df["A"] >= 3) & (df["B"] <= 40), other=replacement_df, inplace=True)
print(df)


df_copy = df.copy()  # Work on a copy to preserve original df
df_copy.where(df_copy["A"] > 100, other=-1, inplace=True)
print("DataFrame modified in-place:")
print(df_copy)
print("-" * 30)


series_A = df["A"]
print(series_A)
series_A.where(series_A > 100, other=-1, inplace=True)
print(series_A)


print(df[df["A"] > 10])
