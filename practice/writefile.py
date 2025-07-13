from pathlib import Path

path = Path.cwd() / "my_folder" / "file2.txt"

list_of_lines = ["\nhi\n", "arpit\n"]

with open(path, mode="a", encoding="utf-8") as file:
    file.writelines(list_of_lines)
