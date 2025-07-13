import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})

# Initialize scaler
scaler = StandardScaler()

# Scale selected columns
df[['Age_scaled', 'Salary_scaled']] = scaler.fit_transform(df[['Age', 'Salary']])

print(df)

scaled_data = scaler.fit(df[['Age','Salary']])
print(scaled_data.scale_)
print(np.std(df['Age']))
print(scaled_data.mean_)
