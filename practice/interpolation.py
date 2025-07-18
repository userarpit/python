import pandas as pd
import numpy as np

# Create a sample Series with NaNs
s = pd.Series([1, 2, np.nan, 4, np.nan, np.nan, 7, 8, np.nan, 10])
print("Original Series:\n", s)
print("-" * 30)

# --- 1. Linear Interpolation (default) ---
# Fills NaN values by drawing a straight line between valid points.
s_linear = s.interpolate(method="linear")
print("Linear Interpolation:\n", s_linear)
# Output explanation:
# s[2] (NaN) -> (2+4)/2 = 3.0
# s[4] (NaN) -> (4+7)/2 = 5.5
# s[5] (NaN) -> (4+7) adjusted linearly = 6.0
# s[8] (NaN) -> No value after it, so remains NaN
print("-" * 30)

# --- 2. Forward Fill (`ffill` or `pad`) ---
# Fills NaN with the last valid observation.
s_ffill = s.interpolate(method="ffill")
print("Forward Fill (ffill):\n", s_ffill)
# Output explanation:
# s[2] (NaN) -> 2.0 (from s[1])
# s[4] (NaN) -> 4.0 (from s[3])
# s[5] (NaN) -> 4.0 (from s[3])
# s[8] (NaN) -> 8.0 (from s[7])
print("-" * 30)

# --- 3. Backward Fill (`bfill` or `backfill`) ---
# Fills NaN with the next valid observation.
s_bfill = s.interpolate(method="bfill")
print("Backward Fill (bfill):\n", s_bfill)
# Output explanation:
# s[2] (NaN) -> 4.0 (from s[3])
# s[4] (NaN) -> 7.0 (from s[6])
# s[5] (NaN) -> 7.0 (from s[6])
# s[0] (NaN if it was) -> 1.0 (no value before, would remain NaN if it was)
print("-" * 30)

# --- 4. Using `limit` and `limit_direction` ---
# Fill only a limited number of NaNs in a specific direction.
s_limit = s.interpolate(method="linear", limit=1, limit_direction="forward")
print("Linear Interpolation with limit=1 (forward):\n", s_limit)
# Output explanation:
# s[2] (NaN) -> 3.0 (from 2.0 and 4.0) - only 1 NaN filled
# s[4] (NaN) -> 5.5 (from 4.0 and 7.0)
# s[5] (NaN) -> remains NaN (as s[4] filled, s[5] is the 2nd consecutive NaN)
# s[8] (NaN) -> remains NaN
print("-" * 30)

# --- 5. Interpolating on a DataFrame ---
df = pd.DataFrame(
    {
        "A": [1, 2, np.nan, 4, 5],
        "B": [np.nan, 10, 11, np.nan, 13],
        "C": [20, np.nan, np.nan, np.nan, 24],
    }
)
print("Original DataFrame:\n", df)
print("-" * 30)

# Default linear interpolation on DataFrame (column-wise)
df_interpolated = df.interpolate(method="linear")
print("DataFrame Linear Interpolation (default axis=0):\n", df_interpolated)
print("-" * 30)

# Interpolate row-wise (filling NaNs across columns)
df_interpolated_rows = df.interpolate(method="linear", axis=1)
print("DataFrame Linear Interpolation (axis=1 - row-wise):\n", df_interpolated_rows)
print("-" * 30)

# --- 6. Time-based Interpolation (requires DatetimeIndex) ---
idx = pd.to_datetime(
    ["2023-01-01", "2023-01-03", "2023-01-06", "2023-01-07", "2023-01-10"]
)
ts = pd.Series([10, np.nan, 30, np.nan, 50], index=idx)
print("Original Time Series:\n", ts)
print("-" * 30)

# 'linear' treats time points as equally spaced (index 0, 1, 2, ...)
ts_linear_interp = ts.interpolate(method="linear")
print("Time Series Linear Interpolation (default):\n", ts_linear_interp)
print("-" * 30)

# 'time' interpolation considers the actual time differences
ts_time_interp = ts.interpolate(method="time")
print("Time Series Time Interpolation:\n", ts_time_interp)
# Output explanation for ts_time_interp:
# 2023-01-03 (NaN): (10 + 30) / 2 = 20.0 (exact midpoint since 01 and 06 are 3 days apart)
# 2023-01-07 (NaN): Value between 30 (on 06) and 50 (on 10).
#                   Days from 06 to 07 = 1 day
#                   Days from 06 to 10 = 4 days
#                   Interpolated value = 30 + (50 - 30) * (1 / 4) = 30 + 20 * 0.25 = 35.0
print("-" * 30)

print(df.interpolate(method="linear", limit_direction="both"))
