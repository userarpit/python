import pathlib
from collections import Counter

entries = pathlib.Path("practice/").iterdir()

extensions = Counter([entry.suffix for entry in entries if entry.is_file()])
print(extensions)