import pandas as pd

# Sample daily sales data
sales_data = pd.Series([10, 12, 15, 13, 18, 20, 22, 19, 25, 28])
sales_data.index = pd.to_datetime(pd.date_range(start='2023-01-01', periods=len(sales_data), freq='D'))
print("Original Sales Data:\n", sales_data)
print("-" * 30)

sma_3_days = sales_data.rolling(window=3).mean()
print(sma_3_days)

# Calculate 3-day Exponential Moving Average (EMA)
ema_3_days = sales_data.ewm(span=3, adjust=False).mean() # adjust=False for classic EMA calculation
print("\n3-Day EMA:\n", ema_3_days)
print("-" * 30)