import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

data = {
    "Complaint_Type": [
        "Defective Product",
        "Slow Delivery",
        "Poor Customer Service",
        "Incorrect Order",
        "Billing Error",
        "Website Glitch",
        "Other",
    ],
    "Count": [150, 120, 90, 60, 40, 30, 10],
}

df = pd.DataFrame(data)

df = df.sort_values(by="Count", ascending=False)
# print(df)
# print(df['Count'].sum())
# print(df['Count'].cumsum())
df["Cumulative_Percentage"] = (df["Count"].cumsum() / df["Count"].sum()) * 100
print(df)
fig, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x="Complaint_Type", y="Count", data=df, ax=ax1, color="skyblue")
ax1.set_title("Complaint Types and Counts")
ax1.set_xlabel("Complaint Type")
ax1.set_ylabel("Number of Complaints")
ax1.tick_params(axis="x", rotation=45)  # Rotate x-axis labels for readability

ax2 = ax1.twinx()
print(type(ax2))
ax2.set_ylabel("Cumulative Percentage")
ax2.tick_params(axis="y", labelcolor="red")
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.plot(
    df["Complaint_Type"],
    df["Cumulative_Percentage"],
    color="red",
    marker="o",
    linestyle="-",
)


print("*" * 100)
for index, row in df.iterrows():
    print(index, row)
    ax2.annotate(
        f"{row['Cumulative_Percentage']:.1f}%",
        (index, row["Cumulative_Percentage"]),
        textcoords="offset points",
        arrowprops={
            "arrowstyle": "->",
            "color": "blue",
            "lw": 1.5,
        },
        xytext=(0, 20),  # Slight offset above the point
        ha="center",
        color="blue",
    )
    
ax2.axhline(80, color='gray', linestyle='--', linewidth=1)
ax2.text(len(df)-1, 80, '80%', va='center', ha='right', backgroundcolor='y', color='gray')


# plt.title('Pareto Chart of Complaint Types')
plt.tight_layout()
plt.show()
