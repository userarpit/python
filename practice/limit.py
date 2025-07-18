import pandas as pd
import numpy as np

s = pd.Series(
    [np.nan, np.nan, 10, np.nan, 20, np.nan, np.nan, np.nan, 30, np.nan, np.nan]
)
print("Original Series:\n", s)
print("-" * 30)

# Interpolate with limit_direction='both' and limit=1
# This will fill any NaN that is next to a valid number.
s_interp_both_limit1 = s.interpolate(
    method="linear", limit=1, limit_direction="both"
)
print("Interpolate with limit=1, limit_direction='both':\n", s_interp_both_limit1)

print("-" * 30)

# Interpolate with limit_direction='both' and no limit (or a sufficiently large one)
s_interp_both_nolimit = s.interpolate(method='linear', limit_direction='both')
print("Interpolate with no limit, limit_direction='both':\n", s_interp_both_nolimit)

print("-" * 30)

# Interpolate with limit_direction='both' and limit=2
s_interp_both_limit2 = s.interpolate(method='linear', limit=2, limit_direction='both')
print("Interpolate with limit=2, limit_direction='both':\n", s_interp_both_limit2)

print("-" * 30)
