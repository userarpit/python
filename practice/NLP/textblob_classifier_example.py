import numpy as np
import pandas as pd
from textblob.classifiers import NaiveBayesClassifier

df = pd.read_csv("spam.csv", encoding="latin-1")
df = df.rename(columns={"v1": "label", "v2": "sms"})
# print(df.head())

train = list(zip(df.sms, df.label))
# print(zipped)
# print(train.shape)
cl = NaiveBayesClassifier(train)

tests = [
    "Convey my regards to him",
    "will of office around 4 pm. now i am going hospital",
]
# pred = cl.predict(tests)
# print(pred)

for sms in tests:
    print(cl.classify(sms))
