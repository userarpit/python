import pandas as pd
import numpy as np

# Levels for the index
countries = ['USA', 'USA', 'USA', 'Germany', 'Germany', 'Germany']
cities = ['New York', 'Los Angeles', 'Chicago', 'Berlin', 'Munich', 'Hamburg']
years = [2020, 2021, 2022, 2020, 2021, 2022]

# Create a MultiIndex
index = pd.MultiIndex.from_arrays([countries, cities, years], names=['Country', 'City', 'Year'])

# Create a Series with this MultiIndex
s = pd.Series(np.random.randint(100, 200, size=6), index=index)
print("Series with MultiIndex:")
print(s)
print("-" * 30)

# Create a DataFrame with this MultiIndex
df = pd.DataFrame(np.random.rand(6, 2) * 100, index=index, columns=['Sales', 'Profit'])
print("DataFrame with MultiIndex (rows):")
print(df)
print("-" * 30)