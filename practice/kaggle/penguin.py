import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")
print(data)
sns.displot(data=data, x="flipper_length_mm", y="bill_depth_mm", hue="species")
plt.show()
