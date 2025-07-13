import pandas as pd

df = pd.DataFrame(
    {
        "weather": [
            "sunny",
            "sunny",
            "overcast",
            "rainy",
            "rainy",
            "rainy",
            "overcast",
            "sunny",
            "sunny",
            "rainy",
        ],
        "temperature": [
            "hot",
            "hot",
            "hot",
            "mild",
            "cool",
            "cool",
            "mild",
            "mild",
            "hot",
            "mild",
        ],
    }
)

df_dummies = pd.get_dummies(df, columns=["weather", "temperature"], drop_first=True).astype(int)
print(df_dummies)
