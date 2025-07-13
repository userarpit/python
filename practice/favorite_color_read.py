from pathlib import Path
import csv

favorites_colors = []

file_path = Path.cwd() / "my_folder" / "favorite_color.csv"

with open(file_path, mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row)
        favorites_colors.append(row)
    
    print(favorites_colors)
