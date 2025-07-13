import pandas as pd
import numpy as np

df_group = pd.DataFrame(
    {"Category": ["A", "A", "B", "A", "B", "B"], "Value": [10, 20, 5, 30, 15, 25]}
)

print(df_group)
print(df_group.groupby("Category")["Value"].cumprod())

print(df_group.shape[1])
