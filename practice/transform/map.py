import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5.5, 6.0, 7.5, 8.0],
    'C': ['apple', 'banana', 'cherry', 'date']
})
print("\nOriginal DataFrame:\n", df)

# Example 1: Rounding all numeric values to 1 decimal place
df_rounded = df.map(lambda x: round(x, 1) if isinstance(x, (int, float)) else x)
print("\nDataFrame with numeric values rounded (using DataFrame.map):\n", df_rounded)
# Output:
#      A    B       C
# 0  1.0  5.5   apple   
# 1  2.0  6.0  banana
# 2  NaN  7.5  cherry
# 3  4.0  8.0    date

# Example 2: Convert all values to string type
df_str = df.map(str)
print("\nDataFrame with all values converted to string:\n", df_str)

# Example 3: Apply a custom function with kwargs
def apply_formatting(value, prefix="Data: "):
    if pd.isna(value):
        return None
    return f"{prefix}{value}"

df_formatted = df.map(apply_formatting, prefix="ID_")
print("\nDataFrame with custom formatting (using DataFrame.map with kwargs):\n", df_formatted)