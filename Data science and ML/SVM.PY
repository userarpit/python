from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("diabetes.csv")
# print(df.head())

x = df[['Pregnancies', 'Insulin', 'BMI', 'Age', 'Glucose', 'BloodPressure', 'DiabetesPedigreeFunction']]  # features
y = df['Outcome']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

model = svm.SVC(kernel='linear')
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

print(y_test)
print(y_predict)

print(f"Accuracy {metrics.accuracy_score(y_test, y_predict):.2f}")

print(model.predict([[4, 5, 30.5, 40, 150, 65, 0.6]]))


