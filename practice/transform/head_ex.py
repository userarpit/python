import pandas as pd
import numpy as np

data = {
    'col1': np.random.randint(0, 100, 20),
    'col2': np.random.rand(20) * 10,
    'col3': [f'cat_{i}' for i in range(20)],
    'col4': pd.to_datetime(pd.date_range('2025-01-01', periods=20, freq='D'))
}
df = pd.DataFrame(data)
print(df.info(verbose=False, memory_usage='deep'))
print(df.info(verbose=False, memory_usage='deep', max_cols=2, show_counts=False))
