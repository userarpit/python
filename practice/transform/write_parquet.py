import pandas as pd
import numpy as np # For NaN values

# Create a sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, np.nan, 35, 28], # np.nan to show nullable dtypes
    'city': ['New York', 'London', 'Paris', 'New York', 'Berlin'],
    'is_active': [True, False, True, np.nan, False] # np.nan for boolean
}
df_original = pd.DataFrame(data)

# Write the DataFrame to a Parquet file
df_original.to_parquet('my_data.parquet', index=False)
print("Original DataFrame written to 'my_data.parquet':\n", df_original)