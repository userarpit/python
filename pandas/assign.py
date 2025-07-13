# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Height': [5.1, 6.2, 5.1, 5.2],
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}


# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Using 'Address' as the column name and equating it to the list
df2 = df.assign(address=['Delhi', 'Bangalore', 'Chennai', 'Patna'])

# Observe the result
print(df2)
