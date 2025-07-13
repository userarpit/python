import pandas as pd
import numpy as np

data = {'col1': [10, 20, 30],
        'col2': [40, 50, 60],
        'col3': ['A', 'B', 'C']}

df = pd.DataFrame(data)
print(df)

# df_values = df.values

df_values = df.to_numpy()
print(df_values)

# series_col1 = df['col1']
# print(series_col1)
# print(series_col1.values)
# print(df_values.dtype)