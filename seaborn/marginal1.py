# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:33:56 2023

@author: HP
"""

import seaborn as sns

df = sns.load_dataset('iris')
print(df)

sns.jointplot(df["petal_length"], df["petal_width"],kind='hex')