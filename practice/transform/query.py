import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age of person": [25, 30, 22, 35, 28],
    "City": ["New York", "London", "Paris", "New York", "London"],
    "Salary": [50000, 60000, 45000, 75000, 55000],
}

df = pd.DataFrame(data)
print(df)
min_age = 20
# df_filtered_age = df.query('Age > @min_age and Salary < 70000')
df_filtered_age = df.query("`Age of person` > @min_age and City not in ['New York', 'London']")
print(type(df_filtered_age))
