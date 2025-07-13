# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:44:55 2023

@author: HP
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("salaries.csv")
x = df['Name']
y = df['Salary']
plt.bar(x,y)
plt.xlabel("Name")
plt.ylabel("Salary")
#print(df)

plt.show()