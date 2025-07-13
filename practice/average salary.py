import pandas as pd
df = pd.read_csv("name_age_salary.csv")
print(df['Salary'].mean())