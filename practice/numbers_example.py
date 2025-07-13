from pathlib import Path
import csv

file_path = Path.cwd() / "my_folder" / "numbers.csv"

numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
with open(file_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)
