# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:12:23 2023

@author: HP
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.random.randint(1,100,10)
print(x)
plt.hist(x,bins=[0,20,40,60,80,100])
plt.show()

#x = np.random.randint(1,100,20)
x = np.array([5,15,5,35,65,55,65,95,85,95])
print(x)
plt.hist(x,bins=10)
plt.show()

df = pd.read_csv("cricket.csv")
x = df['Temp']
y = df['Min']
plt.legend()
plt.hist([x,y])
plt.show()



