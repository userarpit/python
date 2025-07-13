import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
num_sample = 100

# feature 1
study_hours = np.random.normal(10, 2, num_sample)

# feature 2
exam_scores = study_hours * 5 + np.random.normal(5, 10, num_sample)

# feature 3
sleep_hours = np.random.normal(7, 1.5, num_sample)

# feature 4
attendence = np.random.normal(0.8, 0.1, num_sample)
attendence = np.clip(attendence, 0, 1)

data = pd.DataFrame(
    {
        "Study Hours": study_hours,
        "Exam Scores": exam_scores,
        "Sleep Hours": sleep_hours,
        "Attendance": attendence,
    }
)

print("Original dataframe")
print(data.head())

print(data.corr())


scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
# print(data_scaled[:5])
scaled_df = pd.DataFrame(data_scaled, columns=data.columns)
print(scaled_df.head())

print("-" * 50)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(data_scaled)

pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])
print(pca_df.head())

explained_variance = pca.explained_variance_ratio_
print("Explained Variance Ratio of Each Principal Component:")
for i, var in enumerate(explained_variance):
    print(f"Principal Component {i + 1}: {var * 100:.2f}%")
print(f"Cumulative Explained Variance: {explained_variance.sum() * 100:.2f}%")
print("-" * 50)

# plot
plt.figure(figsize=(10, 7))
sns.scatterplot(x="PC1", y="PC2", data=pca_df, alpha=0.7, s=100, edgecolor="r")
plt.title("2 Principal Components of Student Performance Data", fontsize=16)
plt.xlabel(
    f"Principal Component 1 ({explained_variance[0] * 100:.2f}% Variance)", fontsize=12
)
plt.ylabel(
    f"Principal Component 2 ({explained_variance[1] * 100:.2f}% Variance)", fontsize=12
)
plt.grid(True)
plt.axhline(1, color="yellow", linestyle="--", linewidth=0.8)
plt.axvline(0, color="blue", linestyle="--", linewidth=0.8)
plt.show()

print(pca.components_)