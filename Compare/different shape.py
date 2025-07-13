import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

initial_version = Path.cwd() / "Files" / "Different_Shape_1.xlsx"
updated_version = Path.cwd() / "Files" / "Different_Shape_2.xlsx"
df_initial = pd.read_excel(initial_version)
df_updated = pd.read_excel(updated_version)

df_initial.head(3)
df_updated.head(3)
print(df_initial)
print(df_updated)

#print(df_initial.shape)
#print(df_updated.shape)
#print(df_initial.shape == df_updated.shape)
df_updated = df_updated.reset_index()
#print(df_updated)

df_diff = pd.merge(df_initial,df_updated,how="outer",indicator="Exist")
df_diff = df_diff.query("Exist != 'both'") 
#print(df_diff)

df_highlight = df_diff.query("Exist == 'right_only'") 
#print(df_highlight)

highlight_rows = df_highlight['index'].tolist()
highlight_rows = [int(row) for row in highlight_rows]
#print(highlight_rows)

first_row_in_excel = 2

highlight_rows = [x + first_row_in_excel for x in highlight_rows]
#print(highlight_rows)

with xw.App(visible=False) as app:
 
    updated_wb = app.books.open(updated_version)
    updated_ws = updated_wb.sheets(1)
    rng = updated_ws.used_range

    for row in rng.rows:
        if row.row in highlight_rows: 
            row.color = (255,71,76)
    
    updated_wb.save(Path.cwd() / "Files" / "Difference.xlsx")