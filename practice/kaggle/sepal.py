import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("iris")
print(df.head())

# plt.hist(df['sepal_width'])
sns.kdeplot(data=df, x='sepal_width', fill=True)
sns.kdeplot(data=df, x='sepal_length', fill=True)
plt.title("Sepal Width Distribution")
plt.xlabel("Sepal Width")
plt.ylabel("Density")
# plt.legend()
plt.show()