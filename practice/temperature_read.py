from pathlib import Path
import csv

file_path = Path.cwd() / "my_folder" / "temperature.csv"
daily_temp = []
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        daily_temp.append(int_row)

print(daily_temp)