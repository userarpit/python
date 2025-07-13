# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:59:54 2023

@author: HP
"""

import seaborn as sns
import matplotlib.pyplot as plt

tips_data = sns.load_dataset('tips')

# sns.despine()
sns.set_style("whitegrid", {"grid.color": ".6", "grid.linestyle": ":"})
sns.countplot(x='smoker',data=tips_data)
plt.show()
# print(df)
#sns.stripplot(x="day",y="total_bill",data=df)
#sns.stripplot(x='petal_length',y='petal_width',data=df)
# sns.swarmplot(x="day",y="total_bill",data=df)
# plt.show()