# importing pandas module
import pandas as pd

# making data frame from csv file
df = pd.read_csv("nba.csv", index_col ="Name" )
print(df)
print(df.loc[['Jae Crowder','Tibor Pleiss'],['Age','Height','Salary']])
print(df.iloc[3])