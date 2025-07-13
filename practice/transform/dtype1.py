import pandas as pd
from pandas.api.types import CategoricalDtype

data = {"col1": [1, 2, 3], "col2": ["4", "5", "6.7"], "col3": [True, False, True]}

df = pd.DataFrame(data)
print(df.dtypes)
df = df.astype("str")
print(df.dtypes)
print(df)

df_new = pd.DataFrame(
    {
        "ID": ["A1", "B2", "C3"],
        "Value": ["100", "200", "300"],
        "DateStr": ["2023-01-01", "2023-01-02", "2023-01-03"],
    }
)

print("Original dtypes:\n", df_new.dtypes)

convert_dict = {
    "ID": "category",
    "Value": "int",
    "DateStr": "datetime64[ns]",
}

df_new = df_new.astype(convert_dict)
print(df_new.dtypes)

print("*" * 100)

df_cat = pd.DataFrame({"Size": ["M", "L", "S", "M", "XL"]})
size_order = CategoricalDtype(categories=["S", "M", "L", "XL"], ordered=True)
df_cat["Size"].astype(size_order)
print(df_cat["Size"].dtype)

print("*" * 100)

df_err = pd.DataFrame({"A": ["1", "2", "abc", "4"]})

try:
    df_err["A"] = df_err["A"].astype("int", errors="ignore")
except ValueError as e:
    print(e)

print(df_err.dtypes)
print(df_err)

df_err["A"] = pd.to_numeric(df_err["A"], errors="coerce")
print(df_err)
