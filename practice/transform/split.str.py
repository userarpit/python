import pandas as pd
import numpy as np

data = {
    "Full_Name": [
        "John Doe",
        "Jane Smith",
        "Alice Wonderland",
        "Bob The Builder",
    ],
    "Email": [
        "john.doe@example.com",
        "jane_smith@domain.net",
        "alice@company.org",
        "bob@builder.co.uk",
    ],
    "Path": [
        "/users/john/docs/file.txt",
        "C:\\Program Files\\app\\data.csv",
        "/home/jane/photos",
        "/mnt/backup/archive.zip",
    ],
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "=" * 50 + "\n")

df[["first", "second"]] = df["Full_Name"].str.split(" ", n=1, expand=True)
print(df)

df[["username", "Domain"]] = df["Email"].str.split("@", expand=True)
# print(df[['Email', 'email parts']])

# print(df['email parts'][1][1])

print(df)

df['Path_Split_Limited'] = df['Path'].str.split('/', n=2)
print(df[['Path', 'Path_Split_Limited']])
print("\n" + "-"*30 + "\n")
