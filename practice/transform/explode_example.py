import pandas as pd

df_list = pd.DataFrame({
    'ID': [1, 2, 3],
    'Tags': [['apple', 'banana'], ['orange'], ['apple', 'grape', 'kiwi']]
})

print("Original (List in Column):")
print(df_list)

df_exploded = df_list.explode('Tags')

print("\nExploded:")
print(df_exploded)