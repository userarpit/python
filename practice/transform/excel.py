import pandas as pd

df_summary = pd.DataFrame(
    {
        "A": ["Report Date: 2023-01-15", None, None, None, "Product Sales Overview"],
        "B": [None, None, None, None, None],
        "C": [None, None, None, None, None],
        "D": [None, None, None, None, None],
    }
)

# print(df_summary)

df_data = pd.DataFrame(
    {
        "OrderID": [101, 102, 103],
        "Product": ["Laptop", "Mouse", "Keyboard"],
        "Quantity": [1, 2, "N/A"],
        "Price": [1200, 25, 75],
        "Date": ["2023-01-01", "2023-01-01", "2023-01-02"],
    }
)
# print(df_data)


region_data = pd.DataFrame({"Region": ["North", "South"], "Revenue": [5000, 7000]})


with pd.ExcelWriter("sales_report.xlsx") as writer:
    df_summary.to_excel(writer, sheet_name="Summary", index=False, header=False)
    df_data.to_excel(writer, sheet_name="Summary", index=False, startrow=6)
    # You can add more sheets here if needed
    # df_other.to_excel(writer, sheet_name='OtherData', index=False)
    # df_summary.to
    region_data.to_excel(writer, sheet_name="Regional", index=False, header=True)

df_sales_summary = pd.read_excel("sales_report.xlsx", sheet_name="Summary", header=6)
print("DataFrame from 'Summary' sheet, header at row 6:")
print(df_sales_summary)

df_sales_cleaned = pd.read_excel(
    "sales_report.xlsx",
    sheet_name="Summary",
    header=6,
    usecols=["OrderID", "Product", "Quantity"],  # Select specific columns
    na_values=["N/A", "None"],  # Treat 'N/A' as NaN
)
print("\nDataFrame with custom NA values and selected columns:")
print(df_sales_cleaned)

all_sheet = pd.read_excel("sales_report.xlsx", sheet_name=None)  # Read all sheets
for sheet_name, sheet_data in all_sheet.items():
    print(f"\nData from sheet: {sheet_name}")
    print(sheet_data)

df_indexed = pd.read_excel(
    "sales_report.xlsx",
    sheet_name="Summary",
    header=6,
    # index_col="OrderID",
    usecols=["Price", "Date"],
    nrows=1,
)
print("\nDataFrame with 'OrderID' as index:")
print(df_indexed)
