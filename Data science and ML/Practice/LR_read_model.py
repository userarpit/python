import pickle
with open("model_pkl", "rb") as file:
    loaded_model = pickle.load(file)
    
# a = [[1500]]
print(loaded_model.predict([[5000]]))  # Predict price for a house with area 1500 sq ft using the loaded model