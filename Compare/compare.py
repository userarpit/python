import pandas as pd
import numpy as np

df_initial = pd.read_excel('Files/Input_1.xlsx')
df_updated = pd.read_excel('Files/Input_2.xlsx')

print(df_initial.equals(df_updated))
print(df_initial.shape)

comparevalues = df_initial.values == df_updated.values

print(comparevalues)

rows,cols = np.where(comparevalues==False)

for item in zip(rows,cols):
    df_initial.iloc[item[0],item[1]] = ' {} --> {}'.format(df_initial.iloc[item[0],item[1]],df_updated.iloc[item[0],item[1]])

df_initial.to_excel('Files/output.xlsx',index=False,header=True)

