import pandas as pd
import numpy as np

data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'price': [1200, 25, 75, 300, 50],
    'quantity': [2, 10, 5, 3, 8],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
}
df = pd.DataFrame(data)

print(df)

new_df = df.assign(Currency='USD')
print(new_df)

df_assigned_total = df.assign(total_value=df['price'] * df['quantity'],
                              Discounted_Price=lambda x: x['price'] * 0.9)

print(df_assigned_total)

new_df_price = df.assign(price=lambda x: x['price'] * 1.05)

print(new_df_price)