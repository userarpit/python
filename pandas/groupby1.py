# importing Pandas 
import pandas as pd 
import numpy as np


# example dataframe 
example = {'Team':['Arsenal', 'Manchester United', 'Arsenal', 
				'Arsenal', 'Chelsea', 'Manchester United', 
				'Manchester United', 'Chelsea', 'Chelsea', 'Chelsea'], 
					
		'Player':['Ozil', 'Pogba', 'Lucas', 'Aubameyang', 
					'Hazard', 'Mata', 'Lukaku', 'Morata', 
										'Giroud', 'Kante'], 
										
		'Goals':[5, 3, 6, 4, 9, 2, 0, 5, 2, 3] } 

df = pd.DataFrame(example) 

print(df) 
total_goals = df['Goals'].groupby(df['Team'])

# printing the means value 
print(total_goals.agg([sum,np.mean]))	

