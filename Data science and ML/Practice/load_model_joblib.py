import joblib

lr = joblib.load("model_joblib.pkl")
print(lr.predict([[5000]]))