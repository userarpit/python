import pandas as pd
import numpy as np

# --- Example 1: Basic Conversion (pandas infers format) ---
print("--- Example 1: Basic Conversion (pandas infers format) ---")
date_strings = ['2023-01-15', '2023/02/20', 'Jan 1, 2024', '03-10-2023'] # Mixed formats
s_dates = pd.Series(date_strings)
dt_series_inferred = pd.to_datetime(s_dates)
print("Original Series of strings:")
print(s_dates)
print("\nConverted Datetime Series (inferred):")
print(dt_series_inferred)
print(f"Data Type: {dt_series_inferred.dtype}") # Will be datetime64[ns]
print("-" * 50 + "\n")
