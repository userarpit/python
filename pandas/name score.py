import pandas as pd
df = pd.read_csv("name_score.csv",header=None,names=["Name","Score"])
print(df)
print()
print(df[df['Score'] == df['Score'].max()]['Name'])