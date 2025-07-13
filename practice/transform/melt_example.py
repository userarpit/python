import pandas as pd
import numpy as np

df_wide = pd.DataFrame({
    'City': ['New York', 'London'],
    'Jan_Temp': [30, 40],
    'Feb_Temp': [35, 42],
    'Mar_Temp': [40, 45]
})

print(df_wide)

df_melted = pd.melt(df_wide, id_vars=['City'], var_name='Month', value_name='Temperature')

print("\nMelted (Long):")
print(df_melted)