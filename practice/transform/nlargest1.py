import pandas as pd
import numpy as np

data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Heidi",
        "Ivan",
        "Judy",
    ],
    "Age": [25, 30, 22, 35, 28, 40, 29, 31, 26, 33],
    "Score": [85, 92, 78, 95, 88, 92, 81, 95, 75, 89],
    "Experience": [2, 5, 1, 8, 3, 10, 4, 6, 2, 7],
}
df = pd.DataFrame(data)

print(df)

# print(df['Score'].nlargest(n=3))

# print(df.nlargest(n=3, columns=["Score", "Age"]))
print(df.nlargest(n=2, columns=["Score"], keep="all"))
