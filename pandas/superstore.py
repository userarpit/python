import pandas as pd


df = pd.read_excel("global_superstore_2016.xlsx")
# print(df.groupby('Order Date')['Quantity'].sum())
grouped_by_year_month = df.groupby(
    [df["Order Date"].dt.year, df["Order Date"].dt.month]
)["Quantity"].sum()

print(grouped_by_year_month)
