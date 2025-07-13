# importing pandas as pd 
import pandas as pd 

# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
		'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
		'score':[90, 40, 80, 98]} 

# creating a dataframe from a dictionary 
df = pd.DataFrame(dict) 

print(df) 
print("*****" * 10)
# iterating over rows using iterrows() function  
for i, j in df.iterrows(): 
    print(i, j) 
    print() 
    # using a itertuples()  
for i in df.itertuples(): 
    print(i) 

print("*****" * 10)
columns = list(df)

for i in columns:
    print(df.loc[2,i])
           