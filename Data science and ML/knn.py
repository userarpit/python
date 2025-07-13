import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

le = preprocessing.LabelEncoder()

weather_encoded = le.fit_transform(weather)
print('weather :',weather_encoded)

temp_encoded = le.fit_transform(temp)
print('temp :',temp_encoded)

play_encoded = le.fit_transform(play)
print('play :',play_encoded)

features = list(zip(weather_encoded,temp_encoded))
print(features)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(features,play_encoded)
print(model.predict([[0,0]]))
print(model.predict([[2,1]]))
print("****" * 10)
