import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'London', 'Paris', 'New York', 'London'],
    'Salary_USD': [50000, 60000, 45000, 75000, 55000],
    'Years_Experience': [2, 5, 1, 8, 3]
}

df = pd.DataFrame(data)
print(df)

df_selected = df.filter(items=['Name', 'Age', 'City'])
print(df_selected)

df_sel_columns = df.filter(like='a', axis=1)
print(df_sel_columns)


df_regex_sel_column = df.filter(regex='USD$', axis=1)
print(df_regex_sel_column)

df_selected_rows = df.filter(items=['A', 'D'], axis='index')
print(df_selected_rows)

print("*" * 100)

df_indexed = pd.DataFrame(data, index=['Emp_A1', 'Emp_B2', 'Candidate_C3', 'Emp_D4', 'Candidate_E5'])
print(df_indexed)

df_index_filer = df_indexed.filter(like='Can', axis=0)
print(df_index_filer)


print(df.loc[:, ['Name', 'Age']])
print(df.filter(regex='a', axis=1))
