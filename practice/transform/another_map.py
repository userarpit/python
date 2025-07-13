import pandas as pd
import numpy as np

# 1. Create a sample pandas Series
s = pd.Series(['Apple wer', 'Banana', 'Orange', 'Apple', 'Grape', 'Banana', 'Mango', np.nan])

print("Original Series:")
print(s)
print("-" * 50)

# 2. Create a dictionary for mapping (old_value: new_value)
# The keys of this dictionary are what we want to find in the Series.
# The values of this dictionary are what we want to replace them with.
replacement_map = {
    'Apple': 'Red Fruit',
    'Banana': 'Yellow Fruit',
    'Orange': 'Citrus Fruit',
    'Grape': 'Purple Fruit'
}

print("\nReplacement Map Dictionary:")
print(replacement_map)
print("-" * 50)

# 3. Apply the map() method to the Series
s_mapped = s.map(replacement_map)

print("\nSeries after mapping (unmatched values become NaN):")
print(s_mapped)
print("-" * 50)

# Observe: 'Mango' (not in map) and 'np.nan' are now NaN.
# If you want to keep the original values for unmatched items:

# Method A: Use .fillna(s) to fill NaNs with original values
s_mapped_keep_original = s.map(replacement_map).fillna(s)
print("\nSeries after mapping, keeping original values for unmatched items (Method A):")
print(s_mapped_keep_original)
print("-" * 50)

# Method B: Using .replace() instead of .map() for this specific case
# replace() automatically preserves unmatched values if `to_replace` is a dictionary
s_replaced = s.replace(replacement_map)
print("\nSeries after using .replace() (automatically preserves unmatched values):")
print(s_replaced)
print("-" * 50)


# Difference between map() and replace() when using a dictionary:
# - map() will turn values not in the dict keys into NaN.
# - replace() will leave values not in the dict keys as they are.
#   So, for your requirement "find in a dictionary as a key and replace with its values",
#   `Series.replace(dictionary)` is often more convenient if you want unmatched values
#   to remain unchanged.

# Let's show this explicitly with an unmatched value that is not NaN
s_with_unmatched = pd.Series(['Apple', 'Unknown Fruit', 'Orange'])

s_map_unmatched = s_with_unmatched.map(replacement_map)
print("\nmap() with unmatched non-NaN values:")
print(s_map_unmatched)

s_replace_unmatched = s_with_unmatched.replace(replacement_map)
print("\nreplace() with unmatched non-NaN values:")
print(s_replace_unmatched)
print("-" * 50)

# Example: Using `na_action='ignore'` for map()
# This will keep existing NaNs in the Series as NaN and not try to map them.
s_mapped_na_ignore = s.map(replacement_map, na_action='ignore')
print("\nSeries after mapping with na_action='ignore':")
print(s_mapped_na_ignore) # Note: 'Mango' still becomes NaN because it's not ignored by na_action, only existing NaNs are.
print("-" * 50)