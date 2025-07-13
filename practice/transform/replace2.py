import pandas as pd

df_text = pd.DataFrame({"Text": ["apple pie", "banana bread", "cherry pie"]})

print(df_text)
df_text["Text"] = df_text["Text"].str.replace("pie", "tart")
print(df_text)
