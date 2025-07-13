import pandas as pd
import numpy as np

# Create a DataFrame with string data
data = {
    'Product': ['Laptop', 'Mouse', 'KEYBOARD', 'Monitor', 'webcam', np.nan],
    'Category': ['Electronics', 'ACCESSORIES', 'Electronics', 'accessories', 'Peripherals', 'COMPUTERS'],
    'Price': [1200, 25, 75, 300, 50, 1500]
}
df = pd.DataFrame(data)
print(df)

df['Product lower'] = df['Product'].str.lower()
df['Category'] = df['Category'].str.upper()
print(df)

df_chars = pd.DataFrame({'Text': ['AAAHelloAA', 'aWorlda', 'Panda']})
print("\nOriginal DataFrame for specific character strip:")
print(df_chars)
print("\n3. Strip specific characters ('A' and 'a') from 'Text' column:")
df_chars['Text_Stripped_Chars'] = df_chars['Text'].str.strip('Aa')
print(df_chars)
print("\n" + "="*50 + "\n")