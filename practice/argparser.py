import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

target_dir= Path(args.path)

# print(target_dir)

if not target_dir.is_dir():
    print("The target directory does not exists")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)