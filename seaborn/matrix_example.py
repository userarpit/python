import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# tips_corr= tips.corr(numeric_only = True)
# print(tips_corr)
# sns.heatmap(tips_corr,annot=True,linewidths=10,linecolor='grey',cmap='cool')

flight_data = sns.load_dataset("flights")
flights_pivot= flight_data.pivot_table(index='month',columns='year',values='passengers')
# sns.heatmap(flights_pivot,annot=True,lw=3,cmap='cool')
sns.clustermap(flights_pivot,cmap='cool')

# tips_data = sns.load_dataset("tips")
# tips_pivot= tips_data.pivot_table(index='day',columns='time',values='tip')
# sns.heatmap(tips_pivot)
# print(tips_data)
# print(tips_data.groupby('day')[['time']])
plt.show()