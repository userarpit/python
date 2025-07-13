import pandas as pd
df = pd.read_csv('nba.csv')
print(df)

df.sort_values(by="Name",ascending=True,inplace=True,axis=0,na_position='first')
print(df)

df.sort_values(by=["Team","Age","Height"],ascending=[False,True,False],inplace=True,axis=0,na_position='last')
print(df)

