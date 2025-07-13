# importing pandas module
import pandas as pd

# importing csv from link
data = pd.read_csv("nba.csv")
print(data)

# concatenating team with name column
# overwriting name column
data["Name"]= data["Name"].str.cat(data["College"], sep =", ",na_rep="no college")

# display
print(data)
data["Name"]= data["Name"].str.cat(data["Salary"].astype(str), sep =", ")
print(data)
