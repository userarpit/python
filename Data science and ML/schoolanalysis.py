import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.plotly as pl
import plotly.offline as of
import cufflinks as cf
import datetime as dt

of.init_notebook_mode(connected=True)
cf.go_offline()

# donations = pd.read_csv("csv/Donations.csv")
# donors = pd.read_csv("csv/Donors.csv")
# project = pd.read_csv("csv/Projects.csv")
# resources = pd.read_csv("csv/Resources.csv")
schools = pd.read_csv("csv/Schools.csv")
# teachers = pd.read_csv("csv/Teachers.csv")


# print(donations.shape)
# # print(donors.shape)
# print(project.shape)
# print(resources.shape)
print(schools.shape)
# print(teachers.shape)
# print(schools.describe())
# 
# print(schools.head())
# 

# data = pd.merge(donations,project, how="inner",on="Project ID")
# data2 = pd.merge(data,donors,how="inner",on="Donor ID")
# data3 = pd.merge(data2,schools,how="inner",on="School ID")
# data4 = pd.merge(data3,teachers,how="inner",on="Teacher ID")
# a = data4.columns.values.tolist()

# print(data4.head(2))
# x = schools['School State'].sort_values
# schools['School State'].value_counts().sort_values(ascending=False).plot(kind="bar")

# # plt.bar(s,)
# plt.show()
# # print(type(schools['School State']))
# # print()
# print(donations['Donation Amount'].describe())

# print(project[['Project Posted Date','Project Fully Funded Date']].head())