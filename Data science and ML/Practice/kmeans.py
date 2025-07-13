import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    confusion_matrix,
    accuracy_score,
    classification_report,
)
from collections import defaultdict
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer

# sample document data
documents = [
    "Machine learning is a fascinating field.",
    "Data science involves a lot of data analysis.",
    "Algorithms are at the heart of machine learning.",
    "Python is a popular programming language for data science.",
    "K-Means is an unsupervised clustering algorithm.",
    "Support Vector Machines are used for classification.",
    "Deep learning is a subset of machine learning.",
    "Natural Language Processing deals with text data.",
    "Web scraping extracts data from websites.",
    "Neural networks are powerful deep learning models.",
]

# pprint(documents)

for i, document in enumerate(documents):
    pprint(f"Document {i + 1}: {document}")

vectorize = TfidfVectorizer(stop_words="english", max_features=1000)
X = vectorize.fit_transform(documents)
print(X.toarray())
print(vectorize.get_feature_names_out())

df = pd.DataFrame(
    X.toarray(),
    columns=vectorize.get_feature_names_out(),
    index=[f"Document {i + 1}" for i in range(len(documents))],
)

# print(df)

# elbow method calculation and its plot

wcss = []
max_k = len(documents) // 2  # Maximum number of clusters
for k in range(1, max_k + 1):
    kmeans = KMeans(n_clusters=k, init="k-means++", n_init=10, max_iter=300, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

print(wcss)

# plot Elbow Method
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_k + 1), wcss, marker="o")
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
plt.xticks(range(1, max_k + 1))
plt.grid()
plt.show()

optimal_k = 2
print("-" * 50)

# perform k means clusturing
model = KMeans(n_clusters=2, init="k-means++", random_state=42, n_init=10, max_iter=300)
model.fit(X)

cluster_labels = model.labels_
print("Cluster Labels:", cluster_labels)

print("--- Document Cluster Assignments ---")
for i, doc in enumerate(documents):
    print(f"Doc {i + 1}: '{doc}' -> Cluster {cluster_labels[i]}")
print("-" * 50)

clusters = defaultdict(list)
for i, label in enumerate(cluster_labels):
    clusters[label].append(documents[i])

print("Clusters:")
pprint(clusters)

if optimal_k > 1 and optimal_k < len(documents):
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(f"Silhouette Score for K={optimal_k}: {silhouette_avg:.4f}")
else:
    print("Silhouette Score not applicable for K=1 or K=N_documents.")
print("-" * 50)