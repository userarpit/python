# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
		'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict, index = [True, False, True, False])

print(df)

# accessing a dataframe using .loc[] function 
print(df.loc[True])

# Applying a boolean mask to a dataframe : 
print(df[[True, True, True, False]])
print("**************" * 6)
# Masking data based on column value: 
print(df['degree'] == 'MBA')

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# using greater than operator for filtering of data
print(data['Age'] > 25)
print("**************" * 6)
# Masking data based on index value : 

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["BCA", "BCA", "M.Tech", "BCA"],
		'score':[90, 40, 80, 98]}


df = pd.DataFrame(dict, index = [0, 1, 2, 3])

mask = df.index > 1

print(df[mask])
print("**************" * 6)
# print(df)
print(df.truncate(before=1,after=2))