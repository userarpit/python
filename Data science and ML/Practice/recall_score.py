import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, confusion_matrix, accuracy_score, classification_report
import numpy as np
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.DataFrame(
    {
        "Age": np.arange(20, 41, 5),
        "Salary": np.arange(50000, 96000, 10000),
        "Bought": np.random.choice([1, 0], 5),
    }
)

print(df)

X = df[["Age", "Salary"]]
y = df["Bought"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print(y_pred)
df_y = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(df_y)

print(recall_score(y_test, y_pred))
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))  
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print(f"{accuracy_score(y_test, y_pred) * 100:.2f}%  Accuracy")
print(classification_report(y_test, y_pred))