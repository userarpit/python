from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sympy import primerange

df = pd.read_csv("diabetes.csv")
# print(df.head())

x = df[['Pregnancies', 'Insulin', 'BMI', 'Age', 'Glucose', 'BloodPressure', 'DiabetesPedigreeFunction']]  # features
y = df['Outcome']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

print(y_test)
print(y_predict)

print("Accuracy:", metrics.accuracy_score(y_test, y_predict))
cnf_matrix = metrics.confusion_matrix(y_test, y_predict)
print(cnf_matrix)

print(model.predict([[4, 5, 30.5, 40, 150, 65, 0.6]]))

sns.heatmap(pd.DataFrame(cnf_matrix))
plt.title('Confusion Matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print(list(primerange(2,1000)))