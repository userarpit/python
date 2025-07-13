# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:49:15 2023

@author: HP
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
# sns.kdeplot(tips['total_bill'])
print(tips)
sns.jointplot(x="total_bill",y="tip",data=tips,kind='reg',color='y')
#print(tips)

#sns.boxplot(x="day", y="total_bill",data=tips,palette = '  rainbow')
#sns.violinplot(x="day", y="total_bill",data=tips,palette = 'rainbow')

# data = np.random.random((4,6))
# #print(data) 
# #print()
# data = data + np.arange(6) / 2
# print(data)

# sns.set_style("ticks")
# sns.boxplot(data=data)
# plt.title("whitegrid")
plt.show()