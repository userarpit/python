from pathlib import Path
import csv

path = Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")

file_path = path / "employees.csv"


def process_row(row):
    row["salary"] = float(row["salary"])
    return row


with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(process_row(row))
