import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = -2 * np.random.rand(100, 2)
X1 = 1 + 2 * np.random.rand(50, 2)
print(X)
print(X1)
X[50:100, :] = X1
print(X)

Kmean1 = KMeans(n_clusters=2)
Kmean1.fit(X)

Kmean1_centers = Kmean1.cluster_centers_
print(Kmean1_centers)
plt.scatter(X[:, 0], X[:, 1], c='b')
plt.scatter(Kmean1_centers[0][0],Kmean1_centers[0][1],c='g',marker = 's',s=200)
plt.scatter(Kmean1_centers[1][0],Kmean1_centers[1][1],c='r',marker = 's',s=200)

print(Kmean1.labels_)
sample_test = np.array([-1.0,2.0])
second_test = sample_test.reshape(1,-1)
print(sample_test.shape)
print(second_test)
print(Kmean1.predict(second_test))
plt.scatter(second_test[0][0],second_test[0][1],c='b')
plt.show()