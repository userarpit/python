import pandas as pd
import numpy as np
import re  # For regex flags

data = {
    "Log_Entry": [
        "User: JohnDoe logged in from IP: 192.168.1.100 at 2025-06-22 10:30:15",
        "User: Jane_Smith logged out from IP: 10.0.0.5 at 2025-06-22 11:45:00",
        "Error: Failed login attempt from 172.16.0.2 at 2025-06-22 12:00:00 (Invalid credentials)",
        "User: Admin logged in from IP: 192.168.1.1",
        "Process Started successfully",  # No matching pattern
        np.nan,  # Missing log entry
    ],
    "Product_Info": [
        "Product Code: P-ABC-123, Version: 1.5, Status: Active",
        "Product Code: K-XYZ-987, Version: 2.0",
        "Gadget: G-111-222",  # Different format
        "Accessory: A-555-444, Version: 1.0",
        np.nan,
        "Device: D-999-000, Status: Pending",
    ],
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "=" * 50 + "\n")

extracted_log = df["Log_Entry"].str.extract(r"User: (.*?) from IP: (.*?)", expand=True)
print(extracted_log)
print("\n" + "-" * 30 + "\n")

print("2. Extracting User, IP, and DateTime with Named Groups:")
pattern = (
    r"User: (?P<Username>.*?) "
    r"logged (?:in|out) from IP: (?P<IP_Address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) "
    r"at (?P<Timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
)
# `(?:in|out)` is a non-capturing group for "in" or "out"
# `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` matches an IP address pattern
extracted_details = df["Log_Entry"].str.extract(pattern, expand=True)
print(extracted_details)
print("\n" + "-" * 30 + "\n")

print("3. Extracting Product Code, Optional Version, and Optional Status:")
# Using `(?:...)` for non-capturing groups around literal text like 'Code: '
# `(?P<Version>.*?)?` makes the version group optional
# `(?P<Status>.*?)?` makes the status group optional
pattern_product = (
    r"(?:Product Code|Gadget|Accessory|Device): (?P<Code>[A-Z]-\w{3}-\d{3})"
    r"(?:, Version: (?P<Version>\d+\.\d+))?"  # Optional Version
    r"(?:, Status: (?P<Status>.*))?"  # Optional Status
)
extracted_product = df["Product_Info"].str.extract(pattern_product, expand=True)
print(extracted_product)
print("\n" + "-" * 30 + "\n")

print("5. Extracting just the first word from 'Log_Entry' (returns Series):")
first_word_series = df["Log_Entry"].str.extract(r"(\w+)")
print(first_word_series)
print("\n" + "=" * 50 + "\n")
