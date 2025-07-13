import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nparray = np.random.rand(10,5)
df = pd.DataFrame(nparray,columns=['a','b','c','d','e'])

# df.plot.line()
df['c'].plot.density()
print(df)
plt.show()