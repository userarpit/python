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
print(df)
df.drop('Product', axis=1, inplace=True)
print(df)
# # df = df['Product', 'Price', 'Quantity', 'OrderDate', 'CustomerRating', 'IsShipped', 'Notes']
# print(df.dtypes)
# print(df.describe(percentiles=[0.1, 0.5, 0.9]))
# print(df["Price"].describe(percentiles=[0.1, 0.5, 0.9]))
# print(df.shape)
# # print(df.columns)
# # print(df.index)

# for i in df.index:
#     print(i)


# print(df[["Price", "Quantity"]])
# print("*" * 50)
# print(df.loc[[0, 3, 6], "Price"])

# print(df[df['Quantity'] == 1])
# print(df.dtypes)
# print(df.memory_usage(deep=True))
# df['OrderID'] = df['OrderID'].astype('Int8')
# df['CustomerRating'] = df['CustomerRating'].astype('float16')
# print(df.memory_usage(deep=True))
