import pandas as pd
import numpy as np

# importing pandas module
import pandas as pd 

# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
				'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
		'Age':[27, 24, 22, 32, 
			33, 36, 27, 32], 
		'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
				'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
		'Qualification':['Msc', 'MA', 'MCA', 'Phd',
						'B.Tech', 'B.com', 'Msc', 'MA']}	

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data1)

print(df,"********",sep="\n") 

# print(df.groupby(['Name','Qualification']).first())
grp = df.groupby('Name',sort=False)
print(grp.get_group('Jai'))

print(grp.aggregate({'Age': np.mean,'Address':np.sum}))

# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
				'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
		'Age':[27, 24, 22, 32, 
			33, 36, 27, 32], 
		'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
				'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
		'Qualification':['Msc', 'MA', 'MCA', 'Phd',
						'B.Tech', 'B.com', 'Msc', 'MA'],
		'Score': [23, 34, 35, 45, 47, 50, 52, 53]} 
	

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data1)

df1 = df[['Name','Age','Score']]
print(df1)


# using transform function
grp = df1.groupby('Name')
sc = lambda x: ((x - x.mean()) / x.std()*10)
print(grp.transform(sc))
print(grp.filter(lambda x: len(x) == 2))


