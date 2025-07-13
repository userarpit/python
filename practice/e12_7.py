from pathlib import Path
import csv

file_path = Path.cwd() / "my_folder" / "scores.csv"
# open the input file, read it; store the value in a list
with open(file_path, mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    score_list = [row for row in reader]

high_score_dict = {}
for item in score_list:
    name = item["name"]
    score = int(item["score"])

    if name in high_score_dict:
        if score > high_score_dict[name]:
            high_score_dict[name] = score
    else:
        high_score_dict[name] = score


output_file_path = Path.cwd() / "my_folder" / "high_scores.csv"
with output_file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "high_scores"])
    writer.writeheader()
    for name in high_score_dict:
        row_dict = {"name": name, "high_scores": high_score_dict[name]}
        writer.writerow(row_dict)
