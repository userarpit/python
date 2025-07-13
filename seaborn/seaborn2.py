# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:20:49 2023

@author: HP
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = sb.load_dataset("anscombe")
print(df)

sb.lmplot(x="x",y="y",data=df)
plt.show()

x=[10,20,30,40]
y=[50,75,65,90]
df1 = pd.DataFrame({"Roll No":x,"Marks":y})
sb.lmplot(x="Roll No",y="Marks",data=df1)
plt.show()