import pandas as pd
import numpy as np

df_main = pd.DataFrame({
    'item': ['A', 'B', 'C'],
    'qty': [10, 20, 30]
}, index=['x', 'y', 'z']) # Custom index

df_lookup = pd.DataFrame({
    'price': [1.0, 2.5, 3.0],
    'tax_rate': [0.05, 0.08, 0.07]
}, index=['y', 'z', 'a']) # Overlapping and non-overlapping indices

print(df_main)
print(df_lookup)

result_join_default = df_main.join(df_lookup, how="left")
print(result_join_default)

print("*" * 100)
df_lookup_item_index = pd.DataFrame({
    'description': ['Apple Desc', 'Orange Desc', 'Banana Desc'],
    'category': ['Fruit', 'Fruit', 'Fruit']
}, index=['A', 'B', 'D']) # Items A, B from df_main, D is new

df_another_main = pd.DataFrame({
    'product code': ['A', 'B', 'C'],
    'sales': [100, 150, 200]
})
print(df_lookup_item_index)
print(df_another_main)

df_column_index = df_another_main.join(df_lookup_item_index, on="product code", how="right")
print(df_column_index)