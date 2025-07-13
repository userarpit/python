from pathlib import Path
import csv

favorites_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

file_path = Path.cwd() / "my_folder" / "favorite_color.csv"

with open(file_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=favorites_colors[0].keys())
    writer.writeheader()
    writer.writerows(favorites_colors)
