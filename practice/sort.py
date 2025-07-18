import pandas as pd

# Create a sample DataFrame with some duplicate values
data = {
    'OrderID': [101, 102, 101, 103, 102, 104, 105, 103],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Speaker', 'Keyboard'],
    'Price': [1200, 25, 1200, 75, 25, 300, 50, 75],
    'Quantity': [1, 2, 1, 1, 2, 1, 1, 1]
}
df = pd.DataFrame(data)

print(df)

# print(df.sort_index(ascending=False))
print(df.sort_values(by='OrderID', ascending=False))