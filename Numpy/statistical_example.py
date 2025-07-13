import numpy as np
np.random.seed(42)
data = np.random.rand(5, 4) * 100
print(data)

print(np.mean(data, 0))
print(np.std(data))
print(np.median(data, 0))
print(np.max(data))

print(np.min(data))
print(np.percentile(data, 75, axis=0))


# Example 4.4: Correlation Coefficient
# Let's create two 1D arrays (features) and see their correlation
feature1 = np.array([1, 2, 3, 4, 5])
feature2 = np.array([2, 4, 5, 4, 6]) # Slightly correlated with feature1

print("\nFeature 1:", feature1)
print("Feature 2:", feature2)
print("Correlation coefficient between Feature 1 and Feature 2:", np.corrcoef(feature1, feature2))

# For a 2D array, corrcoef returns the correlation matrix
# correlation_matrix[i, j] is the correlation between i-th and j-th columns
print("\nCorrelation Matrix of Data (transposed for column-wise correlation):\n", np.corrcoef(data.T))