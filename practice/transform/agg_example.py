import pandas as pd
import numpy as np

data = {
    "col1": [10, 20, 30],
    "col2": [40, 50, 60],
}

df = pd.DataFrame(data)

print(df)

print(df.agg(total_value1=("col1", "sum"), average_value2=("col2", "mean")))
