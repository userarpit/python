import pandas as pd
import numpy as np

data = {
    "A": [1, 2, np.nan, 4, 5],
    "B": [10, 20, 30, np.nan, 50],
    "C": [100, 110, 120, 130, np.nan],
    "D": ["A", "B", "C", "D", "E"],
}  # No missing values in D

df = pd.DataFrame(data)
print(df)

print(df.count(axis=0))  # Count non-NA/null values across rows
