import csv
from pathlib import Path


class Employee:
    __slots__ = ["name", "age", "job", "salary"]

    def __init__(self, name, age, job, salary):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary

    def profile(self):
        for attr in self.__slots__:
            print(f"{attr.capitalize()}: {getattr(self, attr)}")
        print()


def from_csv_file(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        employees = []
        for row in reader:
            employees.append(
                Employee(
                    name=row["name"],
                    age=int(row["age"]),
                    job=row["job"],
                    salary=float(row["salary"]),
                )
            )
            
        return employees


if __name__ == "__main__":
    path = Path("employee.csv")
    employees_list = from_csv_file(path)
    # for employee in employees_list:
    #     print(employee.name)