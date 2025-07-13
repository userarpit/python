# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:20:29 2023

@author: HP
"""

import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data = np.random.randn(4)
#print(data)
#sb.distplot(data)
#plt.show()

x = [10,5,15,20,7,5]
y = [100,120,150,95,210,50]

data_plot = pd.DataFrame({"Product_no":x,"Cost":y})
print(data_plot)
sb.lineplot(x='Product_no', y='Cost', data=data_plot)
plt.show()
