import numpy as np
import pandas as pd

data = {
    "Region": ["East", "West", "East", "South", "West", "East", "South", "West"],
    "Product": ["A", "B", "A", "C", "B", "C", "A", "A"],
    "Sales": [100, 150, 200, 50, 120, 300, 70, 180],
    "Quantity": [10, 15, 20, 5, 12, 30, 7, 18],
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# df.groupby(by = 'Region').sum(numeric_only=True).plot(kind='bar', title='Total Sales by Region')

# print("DataFrame values shape:", df.values.shape)

grouped_data = (
    df.groupby(by=["Region", "Product"])[["Sales", "Quantity"]].sum().reset_index()
)
print("Grouped DataFrame:\n", grouped_data)
regional_summary = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Average_Quantity=("Quantity", "mean"),
    Num_Products=("Product", "nunique"),  # Count unique products per region
)

print(regional_summary)

diff_min_max = df.groupby("Region").filter(lambda x: x['Sales'].sum() > 200).reset_index(drop=True)
print(diff_min_max)

