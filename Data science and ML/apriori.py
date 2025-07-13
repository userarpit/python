from apyori import apriori

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt

data = pd.read_csv("groceries.csv")
print(data.head())
print(data.shape)

transactions = []
print(data.values[0,1])
for i in range (0,10):
    transactions.append([str(data.values[i,j]) for j in range(0,5)])
    
print(transactions)

rules = apriori(transactions=transactions,min_support = 0.003, 
                min_confidence = 0.2,min_lift = 3, min_length = 2, max_length=2)

associations = list(rules)

print(len(associations))
print(associations[0],"\n",end="\n")
print(associations[1],"\n",end="\n")
print(associations)
# print(associations)