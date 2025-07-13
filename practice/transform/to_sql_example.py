import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text, Integer, String, Date, Float # Import necessary types

# 1. Create a sample DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['Sales', 'Marketing', 'IT', 'Sales', 'HR'],
    'Salary': [60000.00, 75000.50, 80000.00, 62000.75, np.nan], # NaN for Eve's salary
    'HireDate': pd.to_datetime(['2022-01-15', '2021-03-20', '2023-07-01', '2022-11-10', '2024-01-01'])
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "="*70 + "\n")

engine = create_engine(f"mysql+pymysql://root:psra10051986@localhost:3306/world")

try:
    df.to_sql('employee_basic', con=engine, if_exists='replace', index=False)
except Exception as e:
    print(f"Error occurred while writing DataFrame to SQL: {e}")

with engine.connect() as connection:
    query="select * from employee_basic"
    df_from_sql = pd.read_sql(query, connection)
    print("DataFrame read from SQL:")
    print(df_from_sql)


custom_dtypes = {
    'EmployeeID': Integer,
    'Name': String(100),       # Limit string length
    'Department': String(50),  # Limit string length
    'Salary': Float,           # Explicitly float
    'HireDate': Date           # Explicitly date (no time component)
}

df.to_sql('employee_custom', con=engine, if_exists='replace', index=False, dtype=custom_dtypes)
