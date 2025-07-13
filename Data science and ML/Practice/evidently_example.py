import numpy as np
import pandas as pd

# Simulate train (reference) dataset
train_data = pd.DataFrame({
    'age': np.random.normal(30, 5, 500),
    'income': np.random.normal(50000, 5000, 500),
})

print(train_data)