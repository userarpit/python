import pandas as pd
import numpy as np  # For NaN
import re  # Needed for re.IGNORECASE flag for advanced regex

data = {
    "Product_Name": [
        "Laptop Pro",
        "Gaming Mouse",
        "Wireless Keyboard",
        "Monitor Elite",
        "Webcam Basic",
        np.nan,
        "Laptop Air",
    ],
    "Description": [
        "High-performance laptop for professionals.",
        "Ergonomic mouse with customizable buttons.",
        "Mechanical keyboard with RGB lighting.",
        "4K monitor with slim bezels.",
        "HD webcam for video conferencing.",
        "This is a test description.",
        "Ultra-thin laptop for travel.",
    ],
    "Category": [
        "Electronics",
        "Accessories",
        "Electronics",
        "Electronics",
        "Accessories",
        "Miscellaneous",
        "Electronics",
    ],
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "=" * 50 + "\n")

df["Has Laptop"] = df["Product_Name"].str.contains(
    "laptop", case=False, na=False, regex=True
)
print("DataFrame after checking for 'laptop' in 'Product_Name':")
print(df)

# print(df[df['Has Laptop']])
df["Has_Wireless_no_nan"] = df["Product_Name"].str.contains(
    "Wireless", na=False, regex=False
)
print(df)

df["Has Digit"] = df["Description"].str.contains(r"\d", na=False, regex=True)
print("\nDataFrame after checking for digits in 'Description':")
print(df)

df["Description_Has_Laptop_Word"] = df["Description"].str.contains(
    r"\blaptop\b", case=False, na=False, regex=True
)
print(df[["Description", "Description_Has_Laptop_Word"]])
print("\n" + "=" * 50 + "\n")
