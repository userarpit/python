import pandas as pd

tuples= (['USA', 'New York'], ['USA', 'Los Angeles'], ['USA', 'Chicago'])

index_from_tuples = pd.MultiIndex.from_tuples(tuples, names=['Country', 'City'])
print(index_from_tuples)

s_tuple = pd.Series([100,200,300],index=index_from_tuples)
print(s_tuple)

# print(s_tuple[('USA','Chicago')])
# print(s_tuple)

# print(s_tuple.min(level='City'))