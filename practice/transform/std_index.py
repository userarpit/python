import pandas as pd
import numpy as np

arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]
mi = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
s_mi = pd.Series([10, 15, 20, 25], index=mi)
print("MultiIndexed Series:")
print(s_mi)
print("-" * 30)

# Calculate standard deviation at level 'first'
print("Std Dev at level 'first':")
print(s_mi.std(level='first'))
print("-" * 30)