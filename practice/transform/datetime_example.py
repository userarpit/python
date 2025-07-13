import pandas as pd
import numpy as np # For NaN and NaT

# --- Example 1: Basic Conversion (pandas infers format) ---
print("--- Example 1: Basic Conversion (pandas infers format) ---")
date_strings_mixed = [
    '2023-01-15',        # YYYY-MM-DD
    '2023/02/20',        # YYYY/MM/DD
    'Jan 1, 2024',       # Month abbreviation Day, Year
    '03-10-2023',        # MM-DD-YYYY (ambiguous without dayfirst)
    '2025-06-22 21:15:00' # Current time's example from prompt (YYYY-MM-DD HH:MM:SS)
]
s_dates_inferred = pd.Series(date_strings_mixed)
dt_series_inferred = pd.to_datetime(s_dates_inferred, format="mixed")
print("Original Series of strings:")
print(s_dates_inferred)
# print("\nConverted Datetime Series (inferred):")
print(dt_series_inferred)
print(f"Data Type: {dt_series_inferred.dtype}") # Will be datetime64[ns]
# print("-" * 70 + "\n")