import pandas as pd
df = pd.read_csv("employees.csv")
# print(df.count())

class Employee:
    def __init__(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f" {self.name}'s employee id is {self.employee_id} and salary is {self.salary}"
    
employee_list = []
for i in range(50):
    # print(i)
    employee_list.append(Employee(df.loc[i][0],df.loc[i][1],df.loc[i][7]))
print(employee_list[1])


