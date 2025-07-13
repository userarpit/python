import pandas as pd
import numpy as np

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
df3 = pd.DataFrame({"C": [9, 10], "D": [11, 12]})  # Different columns

print(df1)
print(df2)
print(df3)

result_rows = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result_rows)

df4_uneven = pd.DataFrame({'E': [13], 'F': [14]}, index=[0])
print(df4_uneven)

result_cols_inner = pd.concat([result_rows, df4_uneven], axis=1, join="inner")
print(result_cols_inner)