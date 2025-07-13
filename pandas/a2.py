import numpy as np
import pandas as pd

dict_data = {'first_name':['Jason','Molly','Tina','Jake','Amy'],
             'last_name':['Miller','Jacobson','.','Milner','Cooze'],
             'age':[42,52,42,24,73],'pre test score':[4,24,31,".","."],
             'post test score':["25,000","94,000",57,62,70]}

df = pd.DataFrame(dict_data)
# print(df)

df.to_csv("Example.csv",index=False)
df = pd.read_csv("Example.csv",thousands=",")
df.columns = ['First Name','Last Name','Age','Pre Test Score','Post Test Score']

# print(df)

# print(df['First Name'].info())
df["New Age"] = df["Age"] + 1
# print(df)
# print(df[df["Age"] > 50])
# print(df.sort_values(by='Pre Test Score',ascending=False))
# print(df)
print(df.groupby('Age').groups)
print(df['Age'].unique())
