import pandas as pd
import numpy as np

# Sample DataFrame - This data is suitable for pivot because each combination of 'Date' and 'City' is unique
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [30, 60, 32, 65],
    'Humidity': [70, 40, 72, 45]
}
df = pd.DataFrame(data)
print(df)


pivot_temp = pd.pivot_table(df, index='Date', columns='City')
print(pivot_temp)