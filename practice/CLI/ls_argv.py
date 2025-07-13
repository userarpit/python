import sys
from pathlib import Path

if (len := len(sys.argv)) > 2:
    print(f"only one argument is allowed, but got {len - 1} extra arguments")
    sys.exit(1)

if len < 2:
    print("please specify the target directory")
    sys.exit(1)

path = Path(sys.argv[1])
# print(path.is_dir())

if not path.is_dir():
    print("The Target directory does not exists")
    sys.exit(1)

for entry in path.iterdir():
    print(entry.name)
