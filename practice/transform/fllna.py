import pandas as pd
import numpy as np

# s = pd.Series([1, 2, np.nan, 4, np.nan, np.nan, 7, 8])
# print(s)
# # s.fillna(method="ffill", inplace=True)
# # s.fillna(method='bfill', limit=1, inplace=True)
# s.fillna(s.mean(), inplace=True)

# print(s)


df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [11, 12, 13, np.nan, 15],
    'D': [np.nan, np.nan, np.nan, np.nan, np.nan], # All NaN column
    'E': [21, 22, 23, 24, 25] # No NaN column
})

print(df)
# df.fillna(0, inplace=True)
# df.fillna(method='ffill', inplace=True, axis=0)
# df.fillna(method='bfill', inplace=True, axis=0)
# new_df = df.ffill(axis=0)
fill_values = {
    'A': df['A'].mean(),      # Fill 'A' with its mean
    'B': df['B'].median(),    # Fill 'B' with its median
    'C': -1,                  # Fill 'C' with -1
    'D': 'Unknown'            # Fill 'D' with a string
}

df.fillna(fill_values, inplace=True)

# df.fillna(method='bfill', inplace=True, axis=1)
print(df)
