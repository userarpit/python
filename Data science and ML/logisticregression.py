from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("admission.csv")

x = df[['gre', 'gpa', 'rank']]
y = df['admit']

# print(df.head(10))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.50, random_state=0)
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_test)
print(y_pred)
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
sns.heatmap(pd.DataFrame(cnf_matrix))
plt.title('Confusion Matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()

print(model.predict([[690,3.08,3]]))
print(y_test != y_pred)
print(np.mean(y_test != y_pred))
