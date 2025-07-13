from pathlib import Path
import csv

file_path = Path.cwd() / "my_folder" / "numbers.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    numbers = []
    for row in reader:
        numbers.append(row)

    print(numbers)
