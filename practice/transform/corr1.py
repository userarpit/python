import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats

data = {
    "Feature_A": [10, 12, 15, 18, 20, np.nan, 25, 28, 30, 32],
    "Feature_B": [2, 4, 3, 5, 6, 7, 8, 9, 10, 11],
    "Feature_C": [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
    "Category": ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],  # Non-numeric
    "Feature_D": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
}
df = pd.DataFrame(data)

print(df.corr(numeric_only=True))
sns.heatmap(
    df.corr(numeric_only=True, method="kendall"), annot=True, cmap="coolwarm", fmt=".2f"
)
import matplotlib.pyplot as plt

plt.show()

print(df.cov(numeric_only=True))
