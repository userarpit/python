from pathlib import Path
import shutil 

path1 = Path(r"C:\Users\maste")
path2 = Path(r"djangotutorial\pediatrics\urls.py")
# path2 = Path.cwd()
# path = path1 / path2
path = path1.joinpath(path2)
# path = Path.cwd()

# print(type(path))
print(path)
print("-----")
# print(path.resolve())

for dir in path.parents:
    print(dir)

print(path.parent)
print(path.anchor)
print(path.name)
print(path.stem)
print(path.suffix)
newpath = path / "hello.txt"
print(newpath.exists())
print(path.is_file())
print(path.is_dir())

file_path = Path.cwd() / "my_folder"
# if not file_path.exists():
file_path.mkdir(exist_ok=True)

print(file_path.exists())
print(file_path.is_dir())

file_path = Path.cwd() / "my_folder" / "my_subfolder1" / "my_subfolder2"
new_file_path = file_path / "hello.txt"

file_path.mkdir(parents=True, exist_ok=True)
new_file_path.touch()
# print(new_file_path.exists())

print("*" * 50)

path = Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")
# for p in path.iterdir():
#     print(p)

# for p in path.glob("*.txt"):
#     print(p)

paths = [
    path / "program1.py",
    path / "program2.py",
    path / "my_subfolder1" / "program3.py",
    path / "my_subfolder1" / "my_subfolder2" / "image1.jpg",
    path / "my_subfolder1" / "my_subfolder2" / "image2.jpg",
]

for p in paths:
    p.touch()


for p in path.rglob("*.py"):
    print(p)

print("-" * 100)
for p in path.glob("?y_subfolder?"):
    print(p)

print(path)

source = path / "program1.py"
destination = path / "my_subfolder1" / "program1.py"

if not destination.exists():
    source.replace(destination)

source = path / "my_subfolder2"
destination = path / "my_subfolder3"
if not destination.exists():
    source.replace(destination)

delete_file = path / "program2.py"
delete_file.unlink(missing_ok=True)

remove_dir = path / "a"
# remove_dir.rmdir()

shutil.rmtree(remove_dir)