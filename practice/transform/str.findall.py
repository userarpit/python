import pandas as pd
import numpy as np
import re # For regex flags

data = {
    'Text': [
        'apple banana apple orange',
        'red green blue yellow',
        'one two one three four',
        'hello world',
        'multiple apples and multiple bananas',
        np.nan # Missing value
    ],
    'Codes': [
        'ABC-123, XYZ-456, DEF-789',
        'GHI-001',
        'JKL-111, MNO-222',
        'PQR-333',
        'STU-444, VWX-555, YZA-666',
        np.nan
    ]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# df['words'] = df['Text'].str.findall(r'\b\w+\b')
# df['words'] = df['Text'].str.findall('apple')
# df['numbers'] = df['Codes'].str.findall(r'\d+', flags=re.IGNORECASE)
df['found_specific_codes'] = df['Codes'].str.findall(r'[A-Z]{3}-\d{3}')
print(df)