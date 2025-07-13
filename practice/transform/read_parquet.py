import pandas as pd

df = pd.read_parquet("my_data.parquet", engine='pyarrow', use_nullable_dtypes=True)  # Specify the engine if needed
# print(df.describe())
print(df.dtypes)