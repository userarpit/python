import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

# Encode categorical data
data = pd.DataFrame(
    {
        "income": ["High", "Medium", "Low", "High", "Low"],
        "credit": ["Good", "Good", "Fair", "Fair", "Poor"],
        "loan": ["Yes", "Yes", "No", "Yes", "No"],
    }
)

# le = LabelEncoder()
# X = data[["income", "credit"]].apply(le.fit_transform)
# # y = le.fit_transform(data["loan"])

# print(data)
le = LabelEncoder()
X = data[["income", "credit"]].apply(le.fit_transform)
y = data[["loan"]].apply(le.fit_transform)
# print(X)
# print(y)

model = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), n_estimators=2, learning_rate=1
)
model.fit(X, y)

new_case = pd.DataFrame([['Low', 'Poor']], columns=["income", "credit"])
print(new_case)
new_case_encoded = new_case.apply(le.fit_transform)
print(new_case_encoded)

print(model.predict(new_case_encoded))
