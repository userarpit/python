import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.tree import plot_tree

# np.random.seed(42)
data = {
    "Age": [25, 30, 22, 45, 35, 28, 50, 60, 23, 33],
    "Income": np.random.choice(["High", "Medium", "Low"], 10),
    "Student": np.random.choice(["Yes", "No"], 10),
    "Buys_product": np.random.choice(["Yes", "No"], 10),
}

df = pd.DataFrame(data)
print(df)

X = pd.get_dummies(
    df[["Age", "Income", "Student"]], columns=["Income", "Student"]
).astype(int)
print(X)


y = df["Buys_product"].apply(lambda x: 1 if x == "Yes" else 0)
print(y)

x_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)

model.fit(x_train, y_train)

# make prediction of test data
y_pred = model.predict(X_test)

# get accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.title("Confusion Matrix")
# plot_tree(
#     model,
#     feature_names=X.columns.tolist(),
#     class_names=["No Buys", "Buys"],
#     filled=True,  # Fill nodes with colors to indicate majority class
#     rounded=True,  # Round node corners
#     proportion=True,  # Show proportion of samples
#     impurity=True,  # Show impurity at each node
#     fontsize=10,
# )
plt.show()
