import pandas as pd
import numpy as np

data = {
    "Description": [
        "Blue Car 2023",
        "Red Truck 2024 (Damaged)",
        "Yellow Bike (New)",
        "Green SUV",
        "Purple Van (Old Model)",
        np.nan,  # Missing value
    ],
    "Product_Code": [
        "PROD_A-123",
        "prod_b-456",
        "ITEM-789",
        "Prod_C_321",
        "Item_XYZ",
        "MISSING_CODE",
    ],
}
df = pd.DataFrame(data)
# print(df)

# df["Description"] = df["Description"].str.replace("Car", "Vehicle", regex=False)
# print(df)
df["Description_Replace_All_o"] = df["Description"].str.replace("a", "X", case=False, regex=False, n=2)
print(df)
print("\n" + "-" * 30 + "\n")

text_series = pd.Series(['apple banana apple orange', 'grape apple apple'])
print("Original Series:")
print(text_series)
print("\n5. Replacing only the first 'apple' with 'pear':")
text_series_first = text_series.str.replace('apple', 'pear', n=1, regex=False)
print(text_series_first)
print("\n" + "-"*30 + "\n")
