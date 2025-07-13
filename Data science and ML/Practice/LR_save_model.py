import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle

df = pd.read_csv("house_price.csv")
print(df)

X = df[["area"]]
# print(type(X))
y = df["price"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X.to_numpy(), y)

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)


print("Mean Squared Error:", mse)
print("R^2 Score (Accuracy):", r2)

print(model.predict([[1500]]))  # Predict price for a house with area 1500 sq ft
with open("model_pkl", "wb") as file:
    pickle.dump(model, file)
