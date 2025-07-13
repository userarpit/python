from pathlib import Path

path = Path.cwd() / "my_folder"

file_path = path / "file2.txt"
# file = file_path.open(mode="r", encoding="utf-8")
# file = open(file_path, mode="r", encoding="utf-8")

with open(file_path, mode='r', encoding="utf-8") as file:
    for line in file.readlines():
        print(line,end="")