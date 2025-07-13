import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Age": [25, 30, 22, 30, 28, 25],
    "City": ["New York", "London", "Paris", "New York", "London", "Berlin"],
    "Score": [85, 92, 78, 92, 90, np.nan],
}

df = pd.DataFrame(data)
print(df)
df.sort_values(by=["Age", 'Name'], ascending=[True,False], na_position="last", inplace=True)
print(df)

print("*" * 100)

df_indexed = pd.DataFrame({
    'Value': [10, 20, 30, 40],
    'Status': ['Good', 'Bad', 'Good', 'Neutral']
}, index=['Zeta', 'Alpha', 'Gamma', 'Beta']) # Unsorted alphabetical index

print(df_indexed)
print(df_indexed.sort_index(ascending=True, axis=1))  # Sort by index in descending order