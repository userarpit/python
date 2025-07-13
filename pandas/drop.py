# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )

# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)

# display
print(data)

# dropping passed values
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter"], inplace = True)

# display
# print(data.loc[0,:])
print(data.iloc[0,:])

