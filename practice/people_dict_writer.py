from pathlib import Path
import csv

path = Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")

people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24},
]
file_path = path / "people.csv"

with open(file_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=people[0].keys())
    writer.writeheader()
    writer.writerows(people)
