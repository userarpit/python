import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # Often useful for creating dataframes

# 1. Create some sample data (e.g., a correlation matrix)
data = np.random.rand(5, 5) # 5x5 matrix of random numbers
# print(data)
df = pd.DataFrame(data, columns=[f'Feature_{i+1}' for i in range(5)],
                  index=[f'Feature_{i+1}' for i in range(5)])
print(df)
# # Make it look more like a correlation matrix (symmetric with 1s on diagonal)
correlation_data = df.corr() # This will create actual correlations if df had more varied data
# For a quick demo, let's just make a symmetric matrix
print(type(correlation_data))
correlation_matrix = np.array([
    [1.0, 0.7, 0.2, 0.5, 0.1],
    [0.7, 1.0, 0.3, 0.6, 0.2],
    [0.2, 0.3, 1.0, 0.8, 0.4],
    [0.5, 0.6, 0.8, 1.0, 0.9],
    [0.1, 0.2, 0.4, 0.9, 1.0]
])
correlation_df = pd.DataFrame(correlation_matrix,
                              columns=[f'Var_{i+1}' for i in range(5)],
                              index=[f'Var_{i+1}' for i in range(5)])

print(correlation_df)
# # 2. Create the heatmap
plt.figure(figsize=(8, 6)) # Set the figure size for better readability
sns.heatmap(correlation_data,
            annot=True,     # Show the correlation values on the heatmap
            cmap='coolwarm',# Choose a colormap ('coolwarm' is good for correlations)
            fmt=".2f",      # Format the annotations to two decimal places
            linewidths=5,  # Add lines between cells
            cbar=True       # Show the color bar
           )

# # 3. Add title and display
plt.title('Sample Correlation Heatmap')
plt.show()