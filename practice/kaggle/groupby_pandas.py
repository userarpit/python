import pandas as pd


def range_fn(x):
    print(x)
    print("-" * 100)
    print(x.sort_values("Value2", ascending=False))
    return x["Value1"].max() - x["Value1"].min()


data = {
    "Category": ["A", "A", "B", "B", "C", "C"],
    "Value1": [10, 15, 40, 25, 30, 35],
    "Value2": [1, 2, 3, 4, 5, 6],
}

df = pd.DataFrame(data)
print(df)
print(df.groupby("Category")["Value2"].max())
# print("*" * 100)
# result = df.groupby("Category").apply(range_fn)
# print(result)

df_groupby = df.groupby('Category').groups
print("_" * 100)
print(df_groupby)

print("_" * 100)
# for name, group in df_groupby:
#     print(name)
#     print(group['Value1'])
#     print("*" *100)
