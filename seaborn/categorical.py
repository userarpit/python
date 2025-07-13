import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset("tips")
# print(tips.head())
# sns.countplot(x="time",data=tips)
# sns.pointplot(x='day',y="total_bill",data=tips)
# sns.swarmplot(x='smoker',y="tip",data=tips,hue='sex',palette = 'cool')
# sns.pointplot(x='smoker',y="tip",data=tips,hue='sex',palette = 'cool')
# sns.boxplot(x='smoker',y="tip",data=tips,hue='sex',palette = 'cool')
sns.violinplot(x='smoker',y="tip",data=tips,hue='sex',palette = 'cool')
plt.show()