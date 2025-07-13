import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# 1. Create a sample DataFrame
data = {'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse'],
        'Price': [1200, 25, 75, 1300, 250, 30]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("-" * 30)

# 2. Initialize the OneHotEncoder
#    - handle_unknown='ignore': If a category appears in test data that wasn't in train data,
#      it will output all zeros for that feature instead of raising an error.
#    - sparse_output=False: Returns a dense NumPy array instead of a sparse matrix.
#      Set to True for large datasets or many categories for memory efficiency.
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# 3. Reshape the column for the encoder
#    sklearn's encoders expect a 2D array-like input (e.g., a DataFrame column is 1D)
#    So, we reshape it using .values.reshape(-1, 1)
product_column = df[['Product']] # Select as a DataFrame (2D)

# 4. Fit the encoder to learn the categories and then transform the column
#    - fit(): Learns the unique categories from the 'Product' column.
#    - transform(): Converts the categories into one-hot encoded numerical format.
encoded_features = encoder.fit_transform(product_column)

print("\nEncoded Features (NumPy Array):")
print(encoded_features)
print("-" * 30)

# 5. Get the new feature names (column names)
#    The 'feature_names_out_' attribute is available after fitting.
#    We pass the original column name to get sensible new column names.
feature_names = encoder.get_feature_names_out(['Product'])

print("\nNew Feature Names:")
print(feature_names)
print("-" * 30)

# 6. Create a DataFrame from the encoded features
encoded_df = pd.DataFrame(encoded_features, columns=feature_names, index=df.index)

print("\nEncoded Features as a DataFrame:")
print(encoded_df)
print("-" * 30)

# 7. Combine with the original DataFrame (dropping the original categorical column)
df_final = pd.concat([df.drop('Product', axis=1), encoded_df], axis=1)

print("\nFinal DataFrame with One-Hot Encoded 'Product' Column:")
print(df_final)
print("-" * 30)