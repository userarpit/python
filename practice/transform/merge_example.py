import pandas as pd
import numpy as np

df_customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df_orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 3, 1, 2, 99], # 99 is a non-match
    'amount': [100.0, 150.0, 200.0, 50.0, 300.0]
})

print(df_customers)
print(df_orders)

result_inner = pd.merge(df_customers, df_orders, on='customer_id', how='inner')
print(result_inner)

result_inner = pd.merge(df_customers, df_orders, on='customer_id', how='left')
print(result_inner)

result_inner = pd.merge(df_customers, df_orders, on='customer_id', how='right')
print(result_inner)


