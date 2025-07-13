import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [10, 20, 30, np.nan, 50],
        'C': [100, 110, 120, 130, np.nan],
        'D': ['apple', 'banana', 'orange', 'apple', 'grape'], # Non-numeric
        'E': [1, 2, 3, 4, 5]} # No missing values
df = pd.DataFrame(data)

print(df)

print(df.sum(axis=1, numeric_only=True, min_count=4, level=1))  # Sum across rows, ignoring non-numeric columns
