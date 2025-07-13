import numpy as np
import pandas as pd

number_list = list(range(1,1001))
# print(number_list)

sr = pd.Series(number_list)
# print(sr)
print(sr.loc[lambda x : ((x % 7) == 0) & ((x % 17) == 0)])
