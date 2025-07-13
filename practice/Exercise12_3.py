from pathlib import Path
import shutil

path = Path.cwd()
new_dir = path / "my_folder"

new_dir.mkdir(exist_ok=True)
paths = [new_dir / "file1.txt",
         new_dir / "file2.txt",
         new_dir / "image1.png"]

for p in paths:
    p.touch()

sub_dir = new_dir / "images"
sub_dir.mkdir(exist_ok=True)

source = new_dir / "image1.png"
destination = new_dir / "images" / "image1.png"
if not destination.exists():
    source.replace(destination)

del_file = new_dir / "file1.txt"
del_file.unlink()

# shutil.rmtree(new_dir)
