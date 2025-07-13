import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "Age": [25, 30, 25, 35, 30],
    "City": ["New York", "Boston", "New York", "San Francisco", "Boston"],
}

df = pd.DataFrame(data)


print(df)
# print(df[df.duplicated(subset=['Name','City'])])
print(df.duplicated(keep=False))
