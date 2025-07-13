import pyperclip
import pandas as pd

print(pyperclip.paste())

df = pd.read_clipboard(sep="\t", header=None, names=["Name", "Age", "City"], dtype={"Name": "str", "Age": "int64", "City": "str"})
print(df)

