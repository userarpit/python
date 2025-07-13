import pandas as pd

df = pd.read_csv("temperature.csv")
warsaw_data = df[df["City"] == "Warsaw"]

print(df.groupby("year")["AverageTemperatureFahr"].max().max())
