import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.offline as po

np_array = np.random.rand(10,3)
df = pd.DataFrame(np_array, columns=['a','b','c'])
print(df)

df.plot(kind='area',stacked=False,  x ='a',y='b')
plt.show()