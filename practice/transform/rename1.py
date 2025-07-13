import pandas as pd

data = {'old_col_A': [1, 2, 3],
        'old_col_B': ['X', 'Y', 'Z'],
        'Another_Column': [10, 20, 30]}

df = pd.DataFrame(data)
print(df)

convert_rename = {
    'old_col_A' : 'new_col_A',
    'old_col_B' : 'B',
    # 'Another_Column' : 'C',
}

rename_index = {
    0: 'first',
    1: 'second'
}
# new_df = df.rename(columns=convert_rename)
new_df = df.rename(index=rename_index, errors="raise")
# new_df = df.rename(index=lambda x: f"row_id_{x}")
print(new_df)