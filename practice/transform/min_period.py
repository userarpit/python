import pandas as pd
import numpy as np

df_sparse = pd.DataFrame({
    'X': [1, 2, 3, 4, np.nan, np.nan, np.nan],
    'Y': [10, 20, np.nan, np.nan, 50, 60, np.nan],
    'Z': [100, np.nan, np.nan, np.nan, np.nan, np.nan, 700]
})

print(df_sparse.corr(min_periods=1, numeric_only=True))