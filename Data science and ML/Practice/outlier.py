import numpy as np
import pandas as pd

# prepare the dataset
data = {'feature1': [10, 12, 11, 13, 100, 14, 15, 16, 8, 9],
        'feature2': [20, 22, 21, 23, 24, 25, 26, 27, 28, -50]}
df = pd.DataFrame(data)

# print original dataframe
print("Original DataFrame:")
print(df)

# calculate Q1 and q3
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)  

# print(q1)
# print(q3)
# determine IQR
iqr = q3 - q1
# print(iqr)

# define outlier lower and upper bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# print(lower_bound)
# print(upper_bound)

# # df['']
# # find outlier mask
# outliers_mask = ((df < lower_bound) | (df > upper_bound)).any(axis=1)
# # print(outliers_mask)

# final_df = df[~outliers_mask]
# print(final_df)

#clip the outlier and lower and upper bound values
for col in df.columns:
    df[col] = np.clip(df[col], lower_bound[col], upper_bound[col])

print(df)