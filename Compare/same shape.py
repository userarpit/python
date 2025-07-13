import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

initial_version = Path.cwd() / "Files" / "Input_1.xlsx"
updated_version = Path.cwd() / "Files" / "Input_2.xlsx"
df_initial = pd.read_excel('Files/Input_1.xlsx')
df_updated = pd.read_excel('Files/Input_2.xlsx')

print(df_initial.head(2))
df_updated.head(2)
'''print(df_initial)
print(df_updated)

print(df_initial.shape)
print(df_updated.shape)

diff = df_initial.compare(df_updated,align_axis=1)
print(diff)

diff1 = df_initial.compare(df_updated,align_axis=0)
print(diff1)

diff2 = df_initial.compare(df_updated,keep_shape=True,keep_equal=False)
print(diff2)
'''
diff3 = df_initial.compare(df_updated,keep_shape=True,keep_equal=True)
print(diff3)

with xw.App(visible=False) as app:
    initial_wb = app.books.open(initial_version)
    initial_ws = initial_wb.sheets(1)

    updated_wb = app.books.open(updated_version)
    updated_ws = updated_wb.sheets(1)

    for cell in updated_ws.used_range:
        old_value = initial_ws.range((cell.row,cell.column)).value
        if cell.value != old_value:
            cell.api.AddComment(f"Value from {initial_wb.name}:{old_value}") 
            cell.color = (255,0,0)
    
    updated_wb.save(Path.cwd() / "Files" / "output1.xlsx")