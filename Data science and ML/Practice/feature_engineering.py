import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, np.nan, 45, 28],
    'Gender': ['F', 'M', 'M', 'M', 'F'],
    'City': ['New York', 'Paris', 'London', np.nan, 'London'],
    'Salary': [50000, 60000, 55000, 80000, np.nan]
})

print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
# print(df)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
# print(df)

# # city to unknown
df['City'] = df['City'].fillna('Unknown')
# print(df)
# # gender encoding
df['Gender']=df['Gender'].apply(lambda x: 0 if x == 'M' else 1)
# df = pd.get_dummies(df, columns=['City'])
# print(df)

city_column = df[['City']]  # Select as a DataFrame (2D)
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_feature = encoder.fit_transform(city_column)
# print(encoded_feature)
feature_name = encoder.get_feature_names_out(['City'])
# print(feature_name)
# convert to dataframe
encoded_df = pd.DataFrame(encoded_feature, columns=feature_name, index=df.index)
# print(encoded_df)

final_df = pd.concat([df.drop('City', axis=1), encoded_df], axis=1)
# print(final_df)
final_df['Salaryk'] = final_df['Salary'] / 1000
# print(final_df)

final_df['AgeGroup'] = pd.cut(final_df['Age'], bins=[0,30,40,100], labels=['Young', 'Middle-Aged', 'Senior'], include_lowest=True)
# print(final_df)

# scale Age and Salary
scaler = StandardScaler()
final_df[['Age_scaled', 'Salary_scaled']] = scaler.fit_transform(final_df[['Age', 'Salary']])
print(final_df)