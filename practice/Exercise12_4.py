from pathlib import Path

path = Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")

new_image_dir = path / "images"
new_image_dir.mkdir(exist_ok=True)

for p in path.rglob("*.bmp"):
    p.replace(new_image_dir / p.name)
    