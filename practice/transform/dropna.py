import numpy as np

import pandas as pd

s = pd.Series([1, 2, np.nan, 4, 5, np.nan, 7])

print(s)
s.dropna(inplace=True)
print(s)
