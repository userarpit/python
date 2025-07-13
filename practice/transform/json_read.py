import pandas as pd
import io

json_string = """
[
  {"name": "Alice", "age": 30, "city": "New York"},
  {"name": "Bob", "age": 24, "city": "London"},
  {"name": "Charlie", "age": 35, "city": "Paris"}
]
"""

df = pd.read_json(io.StringIO(json_string), orient="records")

print(df)


json_data_index = """
{
  "row_0": {"name": "Alice", "score": 90},
  "row_1": {"name": "Bob", "score": 85},
  "row_2": {"name": "Charlie", "score": 92}
}
"""

df = pd.read_json(io.StringIO(json_data_index), orient="index")
print(df)

json_data_split = '''
{
  "columns": ["fruit", "color"],
  "index": ["a", "b", "c"],
  "data": [
    ["apple", "red"],
    ["banana", "yellow"],
    ["grape", "purple"]
  ]
}
'''
df_split = pd.read_json(io.StringIO(json_data_split), orient='split')
print("DataFrame with orient='split':\n", df_split)
print("-" * 30)

json_data_columns = '''
{
  "city": {"A": "New York", "B": "London", "C": "Paris"},
  "population": {"A": 8000000, "B": 9000000, "C": 2000000}
}
'''
df_columns = pd.read_json(io.StringIO(json_data_columns), orient='columns')
print("DataFrame with orient='columns':\n", df_columns)
print("-" * 30)

with open('data_lines.json', 'w') as f:
    f.write('{"name": "John", "age": 28}\n')
    f.write('{"name": "Jane", "age": 32}\n')

df_lines = pd.read_json('data_lines.json', lines=True)
print("DataFrame from line-delimited JSON:\n", df_lines)
print("-" * 30)