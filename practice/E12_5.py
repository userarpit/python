from pathlib import Path

words = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager"]

with open(Path.cwd() / "starships.txt", mode="w", encoding="utf-8") as file:
    file.writelines(words)


with open(Path.cwd() / "starships.txt", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
    # print(file.read())

print("*" * 40)
with open(Path.cwd() / "starships.txt", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        if line.startswith("D"):
            print(line, end="")
