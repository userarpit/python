# importing pandas as pd 
import pandas as pd 

# Creating the first Series 
sr1 = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio']) 

# Create the first Index 
index_1 = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5'] 

# set the index of first series 
sr1.index = index_1 

# Creating the second Series 
sr2 = pd.Series(['Chicage', 'Shanghai', 'Beijing', 'Jakarta', 'Seoul']) 

# Create the second Index 
index_2 = ['City 6', 'City 7', 'City 8', 'City 9', 'City 10'] 

# set the index of second series 
sr2.index = index_2 

# Print the first series 
print(sr1) 

# Print the second series 
print(sr2) 

print(pd.concat([sr1,sr2]))
