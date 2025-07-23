import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns

df_2015 = pd.read_csv("2015.csv")
df_2016 = pd.read_csv("2016.csv")
df_2017 = pd.read_csv("2017.csv")
df_2018 = pd.read_csv("2018.csv")
df_2019 = pd.read_csv("2019.csv")
print(df_2015.columns)
# print(df_2016)
# print(df_2017)
# print(df_2018)
# print(df_2019)

# print(df_2015.isnull().sum())
# print(df_2016.duplicated().any())
# df_2015.boxplot(column=['Happiness Score'])
# plt.show()

scaler = StandardScaler()
df_2015["Happiness Score"] = scaler.fit_transform(df_2015[["Happiness Score"]])
print(df_2015["Happiness Score"])

sns.heatmap(df_2015.select_dtypes(exclude='object').corr(), annot=True, cmap='cool')
sns.regplot(x="Economy (GDP per Capita)", y="Happiness Score", data=df_2015)
plt.show()
