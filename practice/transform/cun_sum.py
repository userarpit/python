import pandas as pd
import numpy as np

df_col = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [1, 2, 3],
    'C': [100, 200, 300]
})

print(df_col)

print(df_col.cumsum(axis=1))


df_group = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'A', 'B', 'B'],
    'Value': [10, 20, 5, 30, 15, 25]
})

print(df_group)

print(df_group.groupby('Category')['Value'].cumsum())