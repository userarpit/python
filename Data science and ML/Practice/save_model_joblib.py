import pickle

import joblib

with open("model_pkl", "rb") as file:
    loaded_model = pickle.load(file)

joblib.dump(loaded_model, "model_joblib.pkl")
