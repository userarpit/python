import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("Shopping_CustomerData.csv")
print(df.shape)
print(df.head())

data = df.iloc[:, 3:5].values
print(data[0:5, :])

plt.title("Customer Dendrogram")

dend = shc.dendrogram(shc.linkage(data,method='ward'))
plt.show()

cluster = AgglomerativeClustering(n_clusters=4,affinity='euclidean',linkage='ward')
cluster.fit_predict(data)
print(cluster.labels_)

plt.scatter(data[:,0],data[:,1],c=cluster.labels_,cmap="rainbow")
plt.show()

