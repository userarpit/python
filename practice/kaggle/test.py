import pandas as pd

# import numpy as np
import matplotlib.pyplot as plt

# # a = {"day1": 420, "day2": 380, "day3": 390}

# # df = pd.Series(a)
# # print(df)


# data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# df = pd.DataFrame(data, index="day1 day2 day3".split())
# print(df)
# print(df.to_string())

# print(df.loc[["day1", "day2"]])


df = pd.read_csv("data.csv")
print(df.to_string(index=True))
print(
    pd.options.display.max_rows
)  # 60, return first 5 and last 5 rows, and rest with ... in middle
pd.options.display.max_rows = 9999
# print(df.head())
print("*" * 20)
print(df.info())

# df.dropna(inplace=True)
# df.fillna({"Calories": 130}, inplace=True)
# print(df.info())


# print(df["Calories"].loc[0:4])
x = df["Calories"].mean()
print(x)
# df.fillna({"Calories": x}, inplace=True)
print(df)

print(df["Calories"].mode()[0])
print(df[df.isnull().any(axis=1)])
print(df[df["Pulse"].isnull()])

df.loc[17, "Calories"] = 130
print(df[df.isnull().any(axis=1)])
print("*" * 100)
print(df.index)


# for x in df.index:
#     if df.loc[x, "Calories"]
#         print(df.loc[x])
df.drop(27, inplace=True)
print(df[df.duplicated()])
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)

print(df.corr())
print(df.info())


# df.plot(kind="scatter", x="Duration", y="Maxpulse", color="red")
df['Duration'].plot(kind='hist')
plt.show()

# print(df[0])
print(df.mean())
