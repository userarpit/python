from pathlib import Path
import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
]
file_path = Path.cwd() / "my_folder" / "temperature.csv"

with open(file_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures)
