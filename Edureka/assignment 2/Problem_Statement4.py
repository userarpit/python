import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cereal.csv')
x = df['mfr']
y = df['rating']

plt.scatter(x,y)
plt.xticks(range(0,100))
plt.show()


