import csv
from collections import namedtuple

with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    Employee = namedtuple("Employee", next(reader), rename=True)
    for row in reader:
        employee = Employee(*row)
        print(employee.name, employee.job, employee.email)
        