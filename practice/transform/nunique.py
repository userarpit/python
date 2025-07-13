import pandas as pd
import numpy as np


data = {
    "OrderID": range(101, 126),
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"] * 5,
    "Price": [1200.50, 25.00, 75.25, 300.00, 45.99] * 5,
    "Quantity": [1, 2, 1, 1, 3] * 5,
    "OrderDate": pd.to_datetime(pd.date_range("2024-01-01", periods=25, freq="W")),
    "CustomerRating": [4.5, 3.0, np.nan, 5.0, 4.0] * 5,  # Contains NaN
    "IsShipped": [True, False, True, True, False] * 5,
    "Notes": ["Fast delivery", None, "Good product", "Happy customer", "Return soon"]
    * 5,  # Contains None (will be object dtype)
}

df = pd.DataFrame(data)

print(df['Notes'].nunique(dropna=False))
print(df)
