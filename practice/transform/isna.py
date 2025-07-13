import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, None, np.nan, 7])

print(s)

# print(type(s.isna()))

df = pd.DataFrame(
    {
        "A": [1, 2, np.nan, 4, 5, 1],
        "B": [6, np.nan, 8, 9, 10, 11],
        "C": [11, 12, 13, np.nan, 15, 16],
        "D": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],  # All NaN column
        "E": [21, 22, 23, 24, 25, 26],  # No NaN column
        "F": pd.to_datetime(
            ["2023-01-01", "2023-01-02", pd.NaT, "2023-01-04", "2023-01-05", pd.NaT]
        ),
    }
)
print(df)
print(df.isna().sum())
# print(df.isna().sum().sum())

# print(len(df))

print(round(df.isna().sum() / len(df) * 100, 2))
print(df[df.isna().any(axis=1)])
