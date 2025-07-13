from matplotlib import pyplot as plt
import csv
from pathlib import Path


path = Path(r"C:\Users\maste\Documents\Arpit\Python\Matplotlib")
file_path = path / "pirates.csv"

years = []
global_temp = []
pirates_count = []

with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        years.append(row[0])
        global_temp.append(row[1])
        pirates_count.append(row[2])
    
plt.plot(pirates_count, global_temp, "g-o")
plt.title("Global temperature as a function of pirate population")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature (Celsius)")
plt.savefig("pirates.png")
plt.show()