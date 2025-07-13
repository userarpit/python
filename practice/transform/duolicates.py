import pandas as pd

data = {
    "OrderID": [101, 102, 103, 101, 104, 103, 105],
    "CustomerID": ["A", "B", "C", "A", "D", "C", "E"],
    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Laptop",
        "Monitor",
        "Keyboard",
        "Webcam",
    ],
    "Quantity": [1, 2, 1, 1, 1, 1, 1],
}

df = pd.DataFrame(data)
print(df)

df.drop_duplicates(subset=["OrderID"], inplace=True, ignore_index=True, keep=False)
print(df)
