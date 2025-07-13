import pandas as pd

data = {"A": [10, 20, 30, 40], "B": [5, 15, 25, 35], "C": [1, 2, 3, 4]}

df = pd.DataFrame(data)
print(df)

columns_sum = df.apply(sum)
print(columns_sum)

columns_mean = df.apply(lambda x: x.mean())
print(columns_mean)


def column_summary(column_series):
    return pd.Series(
        {
            "sum": column_series.sum(),
            "mean": column_series.mean(),
            "max": column_series.max(),
            "min": column_series.min(),
            "range": column_series.max() - column_series.min(),
        }
    )


column_stats = df.apply(column_summary)
print(column_stats)
