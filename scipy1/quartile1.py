# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:15:52 2023

@author: HP
"""

import numpy as np

list = [1,3,3,4,5,6,6,7,8,8]
Q1 = np.median(list[:5])
Q2 = np.median(list)
Q3 = np.median(list[5:])

IQR = Q3 - Q1
print(Q1)
print(Q2)
print(Q3)
print(IQR)