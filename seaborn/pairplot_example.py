import seaborn as sns
import matplotlib.pyplot as plt

# dots = sns.load_dataset("dots")
# sns.pairplot(dots)
tips = sns.load_dataset("tips")
x = sns.pairplot(tips,hue='day')
x.map_upper(sns.kdeplot)
plt.show()