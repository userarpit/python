import pandas as pd
import numpy as np

csv_dataframe = pd.read_csv("titanic3.csv")
print(csv_dataframe)
""" print(csv_dataframe[['First Name']])
print(csv_dataframe['Zip code'])
print(sum(csv_dataframe['Zip code'])) """
""" my_list = [1,2,3,4]
print(sum(my_list)) """

# # print(csv_dataframe[['Zip code','First Name']].head(3))
# # print(csv_dataframe.sample(n=2))
# # print(csv_dataframe.shape)
# country = ['India','USA','India','USA','India','USA']
# csv_dataframe['Country'] = country
# # print(csv_dataframe)
# gender = ['M','F','M','F','M','F']
# csv_dataframe['Gender'] = gender
# # print(csv_dataframe)
# del csv_dataframe['Country']
# """ print(csv_dataframe.head(2))
# print(csv_dataframe.tail(3))
#  """
# """ print(csv_dataframe.sort_values('City',ascending=False))
# print(csv_dataframe.nunique()) """
# # print(csv_dataframe.loc[1:4])
# # print(csv_dataframe.loc[:,:])
# print(csv_dataframe.describe())
# print(csv_dataframe[csv_dataframe['State'] == 'SD'])
# print(csv_dataframe.iloc[[1,3,5],[4,1]])