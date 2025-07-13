from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

X, y = load_iris(return_X_y=True)
# print(X)
accuracies = []

for _ in range(500):  # 500 bootstrap samples
    idx = np.random.choice(len(X), size=len(X), replace=True)
    # print(idx)
    X_train, y_train = X[idx], y[idx]
    
    # Out-of-bag evaluation
    oob_idx = np.setdiff1d(np.arange(len(X)), np.unique(idx))
    if len(oob_idx) > 0:
        clf = DecisionTreeClassifier().fit(X_train, y_train)
        acc = accuracy_score(y[oob_idx], clf.predict(X[oob_idx]))
        accuracies.append(acc)

print(f"Accuracy: {np.mean(accuracies):.2f} ± {np.std(accuracies):.2f}")