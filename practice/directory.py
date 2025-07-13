import sys
from pathlib import Path

# print(sys.argv)
args_count = len(sys.argv)
if args_count > 2:
    print(f"one argument expected, got {args_count - 1}")
    raise SystemExit(2)
if args_count < 2:
    print(f"you must spectify the target directory")
    raise SystemExit(2)

target_dir= Path(sys.argv[1])

# print(target_dir)

if not target_dir.is_dir():
    print("The target directory does not exists")
    raise SystemExit(2)

for entry in target_dir.iterdir():
    print(entry.name)