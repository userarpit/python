import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv/Sales Data.csv")
data = df[['Country','Sales']]
data['Sales'] = data['Sales'].astype('int32')
print(data.groupby('Country')['Sales'].mean().round(2))

# data5.plot(kind="bar")
# plt.show()