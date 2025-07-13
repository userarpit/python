import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5, np.nan, 7],
        'B': [np.nan, 10, 11, np.nan, 13, 14, 15],
        'C': [20, np.nan, np.nan, 23, np.nan, 25, 26]}

df = pd.DataFrame(data)
print(df)

df.interpolate(method='linear', inplace=True)  # Linear interpolation
# df.bfill(inplace=True, limit=1)  # Backward fill
# df.ffill(inplace=True)  # Forward fill
print(df)



