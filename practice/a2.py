from tensorflow.keras.datasets import mnist
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# print(X_train[0])
# print(y_train[0])


# print(X_train.shape)

# print(np.array_str(X_train[0]))
# print(y_train.shape)
X_train = X_train / 255
X_test = X_test / 255

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
print(model.summary())