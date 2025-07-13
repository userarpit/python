import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.offline as po

po.init_notebook_mode(connected=True)
cf.go_offline()
# @matplotlib inline
nparray = np.random.rand(10,5)
df = pd.DataFrame(nparray,columns=['a','b','c','d','e'])

# df.plot.line()
# df['c'].plot.bar()
# df.plot.area(stacked=False,alpha=0.1)
# df.plot.box()
df.plot.hexbin(x='a',y='b')
# df.plot(kind='scatter', x='a',y='b')
# df.iplot(kind="surface")
print(df)
plt.show()