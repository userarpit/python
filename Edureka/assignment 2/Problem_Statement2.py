import numpy as np
import pandas as pd

subject = ['English','History','Geography','Mathematics','Science']
students = [{'Sam':60,'Jackson':74,'Ahree':85}, 
                {'Gloria':83,'Sam':65,'Isla':78,'Aron':72,'Gray':61},
                {'Jackson':92,'Gloria':95,'Isla':82,'Aron':75,'Ahree':76},
                {'Sam':99,'Gloria':74,'Jackson':89,'Ahree':85,'Gray':95},
                {'Sam':89,'Aron':82,'Gray':78,'Isla':93,'Ahree':87}]
sr = pd.Series(subject)

# print(sr)
df = pd.DataFrame(students,index=sr)
# print(df)

df.fillna(0,inplace=True)
# print(df)
df_transpose = df.transpose()
# print(df_transpose)
df_transpose['Average'] = df.mean()
print(df_transpose)