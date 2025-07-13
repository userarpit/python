import pandas as pd
import numpy as np

data_duplicates = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01'], # Duplicate Date/City combo
    'City': ['New York', 'New York', 'Los Angeles'],
    'Temperature': [30, 31, 60]
}   
df_duplicates = pd.DataFrame(data_duplicates)
pivot_dup = pd.pivot(df_duplicates, index='Date', columns='City', values='Temperature')
print(df_duplicates)