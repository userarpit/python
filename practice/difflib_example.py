from difflib import get_close_matches
from difflib import HtmlDiff

words = ["disagree", "discover", "display", "disrupt", "distance"]

print(get_close_matches("dis",words))




a = """The cat is sleeping on the red sofa."""
b = """The cat is sleeping on a blue sofa..."""

d = HtmlDiff()
html_diff = d.make_file(a.splitlines(), b.splitlines()) # a,b were defined earlier
with open("diff.html", "w", encoding="utf-8") as f:
    f.write(html_diff)