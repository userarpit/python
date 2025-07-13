import pandas as pd


df = pd.DataFrame({"A": [1, 2, 3, 1], "B": ["cat", "dog", "cat", "bird"]})

print(df)

new_df = df.replace([1, 2], [100, 200])
df_dict_replace = df.replace({"A": {1: "canine"}, "B": {"cat": "feline"}})
print(df_dict_replace)

df_str = pd.DataFrame({'Text': ['apple_1', 'banana_2', 'cherry_3', 'grape_10']})
df_regex_example = df_str.replace(r'\d+', 'X', regex=True)
print(df_regex_example)
