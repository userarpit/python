# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:36:23 2023

@author: HP
"""

from scipy import stats
from scipy.stats import norm
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# x = stats.mode(data)
# print(x)

# t_stat, p_value = stats.ttest.samp(data, popmean=5)
# print(t_stat)
# print(p_value)

print(np.mean(data))
print(np.std(data))

z_score = (data - np.mean(data)) / np.std(data)

print(z_score)
print( 2 * (1- norm.cdf(np.abs(z_score))))