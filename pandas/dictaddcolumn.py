# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Height': [5.1, 6.2, 5.1, 5.2],
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Define a dictionary with key values of
# an existing column and their respective
# value pairs as the # values for our new column.
address = {'Jai': 'Delhi', 'Princi': 'Bangalore',
		'Gaurav': 'Patna', 'Anuj': 'Chennai'}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Provide 'Address' as the column name
df['Address'] = address.values()

# Observe the output
print(df)
