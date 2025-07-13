import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": list(np.random.randint(1, 10, 6)),
        "B": list(np.random.randint(1, 10, 6)),
        "C": [11, 12, 13, np.nan, 15, 20],
        "D": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    }
)
df.loc[[2, 3], "B"] = np.nan
print(df)
# df.dropna(inplace=True, thresh=4, axis=1)
df.dropna(inplace=True, subset=['A','C'])

print(df)
