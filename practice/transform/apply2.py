import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 22, 35],
        "Score1": [85, 92, 78, 95],
        "Score2": [70, 88, 85, 90],
    }
)

print(df)


def age_group(age: int) -> str:
    if age < 25:
        return "Young"
    elif age < 30:
        return "Adult"
    else:
        return "Senior"


df["Age"] = df["Age"].apply(age_group)
print(df)

df["Average_Score"] = df[["Score1", "Score2"]].apply(lambda row: np.mean(row), axis=1)

print(df)

df["High_Achiever"] = df.apply(
    lambda row: "Yes" if row["Average_Score"] > 85 else "No", axis=1
)
print("\nHigh achiever status per row:\n", df)


def calculate_grade(row, bonus_points):
    total_score = (row["Score1"] + row["Score2"] + bonus_points)
    return "A" if (total_score / 2 > 90) else "B"


df["Grade"] = df.apply(calculate_grade, axis=1, bonus_points=5)
print(df)
print(df['Score1'] * 2)
