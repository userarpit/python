import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
from scipy import stats
import numpy as np

df = pd.read_csv("data.csv", encoding="latin-1")
# print(df.head())
# print(df.info())
# print(df['Country'].value_counts())

# remove null data
df.dropna(inplace=True)
# print(df.info())

# convert invoice date to date time object
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# convert CustomerID to Int
df["CustomerID"] = df["CustomerID"].astype(int)

# add Total column
df["Total"] = df["UnitPrice"] * df["Quantity"]
print(df.head())

top_customers = (
    df.groupby("CustomerID")["Total"].sum().sort_values(ascending=False).head(10)
)
# print(top_customers)
# top_customers
top_customers = top_customers.reset_index()
print(top_customers)

top_customers.to_csv("top_customers.csv")

# gather day of week
df["DayofWeek"] = df["InvoiceDate"].dt.dayofweek
# print(df)

# separate data
weekday_purchase = df[df["DayofWeek"] < 5]["Total"]
weekend_purchase = df[df["DayofWeek"] >= 5]["Total"]

# print(weekday_purchase)
# print(weekend_purchase)

t_stat, p_val = stats.ttest_ind(weekday_purchase, weekend_purchase, equal_var=False)

print(f"T-test result values t = {t_stat:.2f}, p = {p_val:.4f}")
# print(np.mean(weekday_purchase.values))
# print(np.mean(weekend_purchase.values))

# Pivot: Customers × Countries with their total spend
df_pivot = df.pivot_table(
    values="Total", index="CustomerID", columns="Country", aggfunc="sum"
).fillna(0)
print(df_pivot)

corr_matrix = df_pivot.corr()
print(corr_matrix)

plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f')
plt.title('Correlation of customer purchase by country')
plt.show()