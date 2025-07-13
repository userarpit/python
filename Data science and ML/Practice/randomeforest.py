import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_diabetes
import seaborn as sns
import matplotlib.pyplot as plt

df = load_diabetes(as_frame=True)
X = df.data
y = (df.target >= np.median(df.target)).astype(int)
print(y)

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train randome forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

#make predictions
y_pred = rf.predict(X_test)

cofusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")  
print(cofusion)

print("Accuracy:", accuracy_score(y_test, y_pred))


plt.figure(figsize=(6,4))
sns.heatmap(cofusion, annot=True, fmt='d', cmap='Blues', xticklabels=['Low', 'High'], yticklabels=['Low', 'High'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')


plt.show()

print(classification_report(y_test, y_pred))