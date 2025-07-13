import pandas as pd
import numpy as np

data_incomplete = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York'], # Los Angeles for 2023-01-02 is missing
    'Temperature': [30, 60, 32]
}
df = pd.DataFrame(data_incomplete)
print(df)
pivot_incomplete = pd.pivot(df, index='Date', columns='City', values='Temperature')
print(pivot_incomplete)