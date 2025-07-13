import pandas as pd

data = {"col1": [1, 2, 3], "col2": ["A", "B", "C"], "col3": [True, False, True]}

df = pd.DataFrame(data)
print(df)

col2_index = df.columns.get_loc('col2')
df.insert(col2_index, "col4", [10, 20, 30])
df.insert(df.shape[1], column='Status', value='Active')

new_series_values = pd.Series([99, 88, 77], index=[2, 1, 0]) # Deliberately mixed up index
df.insert(df.shape[1], column='End', value=new_series_values)
df.insert(df.shape[1], column='End', value=new_series_values, allow_duplicates=True)
print(df)
