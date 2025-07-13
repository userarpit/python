import numpy as np
import pandas as pd

name = ['Amit','Bob','Kate']
pds = pd.Series(name,index = ['r1','r2','r3']) 
pdsnona = pds.dropna()
print(pdsnona.str.lower())
print(pdsnona.str.upper())
print(pdsnona.str.len())
print(pdsnona.str.strip())
print(pdsnona.str.lstrip())
print(pdsnona.str.rstrip())
print(pdsnona.iloc[3:5])
print(pdsnona.loc['r2'])
print(pdsnona.isin(['Bob']))