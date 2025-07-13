import numpy as np

data = np.array([1, 2, 3, 4, 5])
bootstrap_means = []

for _ in range(100):  # 1000 bootstrap samples
    sample = np.random.choice(data, size=len(data), replace=True)
    print(sample)
    bootstrap_means.append(np.mean(sample))

print(f"Estimated mean: {np.mean(bootstrap_means):.2f} ± {np.std(bootstrap_means):.2f}")