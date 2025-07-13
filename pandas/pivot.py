import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df)

print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))


arr = np.random.randn(10)
print(arr.shape)
ts = pd.Series(arr, index=pd.date_range("1/1/2000", periods=10))
print(ts)
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()


df = pd.DataFrame(
    np.random.randn(10, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

print(df)
df = df.cumsum()
print(df)
df.plot()

df.to_parquet("a.parquet")
plt.show()
print("*" * 10)
print(pd.read_parquet("a.parquet"))

