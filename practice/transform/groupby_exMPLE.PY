import pandas as pd
import numpy as np

data = {'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'North', 'South'],
        'City': ['New York', 'Miami', 'Boston', 'London', 'Miami', 'Paris', 'New York', 'Austin'],
        'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A'],
        'Sales': [100, 150, 120, 200, 180, 130, 90, 160],
        'Units': [10, 15, 12, 20, 18, 13, 9, 16]}
df = pd.DataFrame(data)
print(df)

print(df.groupby('Region')['Sales'].sum())
print(df.groupby('Category')['Units'].mean())

count_by_city = df.groupby('City').size() # .size() counts items in each group, including NaN
print("Count of Entries by City:")
print(count_by_city)

total_sales_region_category = df.groupby(['Region', 'Category'])['Sales'].sum().reset_index()
print("Total Sales by Region and Category:")
print(total_sales_region_category)

max_units_region_city = df.groupby(['Region', 'City'])['Units'].max()
print("Max Units by Region and City:")
print(max_units_region_city)
print("-" * 50)
region_sales_stats = df.groupby('Region')['Sales'].agg(['sum', 'mean', 'max', 'min'])
print(region_sales_stats)
                                          
                                          
# Group by 'Region' and 'Category' and sum 'Sales', keeping groups as columns
total_sales_flat = df.groupby(['Region', 'Category'], as_index=False)['Sales'].sum()
print("Total Sales by Region and Category (as_index=False):")
print(total_sales_flat)
print("-" * 50)

# print(df)
df['Avg_Region_Sales'] = df.groupby('Region')['Sales'].transform('mean')  # This will return a Series with the mean sales for each region, aligned with the original DataFrame
print("DataFrame with Average Region Sales:")
print(df)

df['Sales_Deviation_From_Region_Mean'] = df['Sales'] - df['Avg_Region_Sales']
print(df)

top_2_sales_per_region = df.groupby('Region').apply(lambda x: x.nlargest(2, 'Units'))
print("Top 2 Sales Entries per Region:")
print(top_2_sales_per_region)
print("-" * 50)