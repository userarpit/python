import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = sns.load_dataset("tips")
print(df.head())

sns.kdeplot(
    data=df, x="total_bill", y="tip", hue="time", fill=True, common_norm=False, alpha=0.5
)


plt.title("Total Bill Distribution by Time (Lunch vs Dinner)")
plt.xlabel("Total Bill")
plt.show()
