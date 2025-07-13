import pandas as pd
import numpy as np

df_orders_export = pd.read_csv("orders_export.csv")

def check_and_return_value_v2(main_string, value1, value2):
    """
    Checks a main_string for the presence of two specified values (substrings)
    with a new precedence rule for when both are present.

    Args:
        main_string (str): The string to search within.
        value1 (str): The first value (substring) to look for.
        value2 (str): The second value (substring) to look for.

    Returns:
        str or None:
            - value1, if only value1 is present.
            - value2, if only value2 is present.
            - value1, if both are present AND value1 appears AFTER value2.
            - value2, if both are present AND value2 appears AFTER or at the same position as value1.
            - None, if neither value1 nor value2 is present.
    """

    # Find the starting index of each value
    idx1 = main_string.find(value1)
    idx2 = main_string.find(value2)

    contains_value1 = idx1 != -1
    contains_value2 = idx2 != -1

    if contains_value1 and contains_value2:
        # Both are present. Now, check their order.
        if idx1 > idx2:
            return value1 # value1 starts AFTER value2
        else:
            return value2 # value2 starts AFTER or AT THE SAME POSITION as value1
    elif contains_value1:
        return value1  # Only value1 is present
    elif contains_value2:
        return value2  # Only value2 is present
    else:
        return None # Neither value found



column_names = [
    "S No.",
    "Date",
    "Vch/Bill No",
    "Particulars",
    "CGST/SGST",
    "Product Name",
    "Item Details",
    "Size",
    "Qty.",
    "Unit",
    "Price",
    "Amount",
    "COD",
    "Payment",
    "Unnamed: 14",
    "Unnamed: 15",
    "CGST/SGST.1",
]
df_june = pd.DataFrame(columns=column_names)

index = 0

# Get yesterday's date as a pandas Timestamp
yesterday_timestamp = pd.Timestamp.today() - pd.Timedelta(days=1)
yesterday_formatted_string = yesterday_timestamp.strftime("%d-%m-%Y")
data = {}
data["S No."] = "Main"
data["Date"] = yesterday_formatted_string
data["CGST/SGST"] = "I/GST-TaxIncl."
data["Size"] = "Tee & Hoodie"
data["Unit"] = "Pcs."
data["Vch/Bill No"] = None
save_bill_no = None
save_price = 0.00
save_amount = 0.00

df_orders_export["Payment Method"] = df_orders_export["Payment Method"].astype(str)

for idx in df_orders_export.index:
    if data["Vch/Bill No"]:
        if save_bill_no == df_orders_export.loc[idx, "Name"]:
            data["Vch/Bill No"] = np.nan
        else:
            data["Vch/Bill No"] = df_orders_export.loc[idx, "Name"]
            save_bill_no = data["Vch/Bill No"]
    else:
        data["Vch/Bill No"] = df_orders_export.loc[idx, "Name"]
        save_bill_no = data["Vch/Bill No"]

    data["Particulars"] = df_orders_export.loc[idx, "Billing Name"]
    data["Product Name"] = df_orders_export.loc[idx, "Lineitem name"]
    data["Item Details"] = df_orders_export.loc[idx, "Lineitem sku"]

    data["Qty."] = df_orders_export.loc[idx, "Lineitem quantity"]

    data["Price"] = data["Amount"] = df_orders_export.loc[idx, "Lineitem price"]

    data["COD"] = np.nan
    data["Payment"] = np.nan
    data["Unnamed: 14"] = df_orders_export.loc[idx, "Notes"]

    if df_orders_export.loc[idx, "Payment Method"] == "Cash on Delivery (COD)":
        data["COD"] = 100.00
        data["Payment"] = (
            "Shiprocket COD " + df_orders_export.loc[idx, "Shipping Province"]
        )
    elif "manual" in df_orders_export.loc[idx, "Payment Method"].lower():
        data["Payment"] = df_orders_export.loc[idx, "Billing Name"]
    else:  # blank case
        pass

    return_value = check_and_return_value_v2(df_orders_export.loc[idx, "Payment Method"], "Cashfree", "Razorpay")
    
    match return_value:
        case "Cashfree":
            data["Payment"] = "Cashfree " + df_orders_export.loc[idx, "Shipping Province"]
        case "Razorpay":
            data["Payment"] = "Razorpay " + df_orders_export.loc[idx, "Shipping Province"]
        case None:
            pass  # Do nothing if neither is found
    
    df_june.loc[index] = data
    # print(data)
    index += 1

df_june.to_csv("daily.csv", index=False)
print("Updated CSV saved successfully.")
