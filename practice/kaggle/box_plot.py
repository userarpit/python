import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset("iris")
new_data = iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

plt.boxplot(new_data["sepal_width"], patch_artist=True, boxprops=dict(facecolor="blue"))
plt.title("Custom Boxplot of SepalWidthCm")
plt.ylabel("Values")
plt.show()
