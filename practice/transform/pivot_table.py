import pandas as pd
import numpy as np

data = {
    "Region": ["East", "East", "West", "West", "East", "West", "East", "East", "West"],
    "Product": ["A", "B", "A", "C", "A", "B", "C", "B", "A"],
    "Salesperson": [
        "Alice",
        "Bob",
        "Alice",
        "Charlie",
        "Bob",
        "Charlie",
        "Alice",
        "Bob",
        "Charlie",
    ],
    "Month": ["Jan", "Jan", "Feb", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar"],
    "Sales": [100, 150, 200, 120, 180, 250, 90, 160, 220],
    "Units": [10, 15, 20, 12, 18, 25, 9, 16, 22],
}
df = pd.DataFrame(data)

print(df)

pivot_avg_sales = pd.pivot_table(
    df,
    # values=["Sales", "Units"],
    index=["Region", "Salesperson"],
    columns=["Product", "Month"],
    aggfunc={'Sales': 'sum', 'Units': 'mean'},
    margins=True,
    fill_value=0,
)

print(pivot_avg_sales)
