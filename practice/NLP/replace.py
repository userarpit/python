import pandas as pd
import numpy as np
import re # Needed for compiling regex and using re.IGNORECASE flag if desired

# Create a sample Series with text that needs replacements
s = pd.Series([
    'My fav color is red and blue.',
    'I saw a green apple and a red berry.',
    'The Sky is BLUE.',
    'Yellow sun.',
    'purple grapes.',
    np.nan
])

print("Original Series:\n", s)
print("-" * 50)

# Define the dictionary mapping
# Keys are patterns (substrings or regex) to find.
# Values are the strings to replace them with.
replace_map = {
    r'red': 'crimson',
    r'blue': 'azure',
    r'green': 'emerald',
    r'(?i)yellow': 'golden' # Case-insensitive 'yellow'
}

print("\nReplacement Map Dictionary:")
print(replace_map)
print("-" * 50)


# --- Method 1 (Recommended): Using Series.replace(dict, regex=True) ---
# This method is specifically designed for dictionary-based replacements,
# and when regex=True, it applies the regex matching to the dictionary keys.

# It processes the patterns in the order they appear in the dictionary (Python 3.7+ preserves insertion order).
# If patterns overlap, the order might matter.
s_replaced_dict_regex = s.replace(replace_map, regex=True)

print("\nMethod 1: Using s.replace(dict, regex=True):")
print(s_replaced_dict_regex)
print("-" * 50)


# --- Method 2: Using Series.str.replace() with a combined regex and a callable ---
# This is more complex but provides fine-grained control, especially for backreferences.

# 1. Create a combined regex pattern using '|' (OR) from the dictionary keys
# Ensure longer/more specific patterns come first if they can overlap with shorter ones
# The order of `replace_map.keys()` matters here if patterns overlap.
# For example, if you had {'apple': 'fruit', 'pineapple': 'tropical fruit'},
# and 'apple' came first, 'pineapple' might only replace 'pine' leaving 'apple'
# if not careful with word boundaries. For simple cases, key order is usually fine.
combined_pattern = '|'.join(map(re.escape, replace_map.keys())) # re.escape handles special regex chars in keys
# If patterns in keys are *intended* to be regex, don't use re.escape
# e.g., if keys are r'red', r'blue', then just '|'.join(replace_map.keys()) would work.
# But for the mixed case of literals and regex like (?i)yellow, you need more control.

# A more robust combined pattern if keys can contain regex flags:
# For `replace_map` as defined, the following works:
combined_pattern = '|'.join(replace_map.keys())

def replace_with_callable(match):
    """
    Callable function for re.sub.
    It receives a match object and returns the replacement string.
    """
    # match.group(0) is the entire matched string
    matched_text = match.group(0)
    
    # Iterate through the map to find which key matches this matched text
    # This might require careful handling of case/regex flags for keys
    for pattern, replacement in replace_map.items():
        # Re-check match with original pattern to find the exact rule
        # Using re.fullmatch() is safer to ensure the *entire* matched_text
        # corresponds to one of the patterns, considering its own regex flags.
        
        # For simplicity with mixed-case/regex, we apply the regex directly
        # and then lookup. A more robust solution might involve compiling patterns.
        
        # A simpler way when `replace_map` keys are the exact patterns as intended:
        # If the key itself is a regex, you need to compile it or handle flags.
        
        # For our example's `replace_map`, this check is good:
        if re.fullmatch(pattern, matched_text, flags=re.IGNORECASE if '(i)' in pattern else 0):
             return replacement
    
    return matched_text # Should not happen if all matches are covered by map

# Note: The `regex=True` parameter in str.replace() is implied when using `pat` as string.
# We also need to use `na=False` or `fillna('')` if we want to process NaNs.
s_replaced_str_callable = s.str.replace(combined_pattern, replace_with_callable, regex=True)

print("\nMethod 2: Using s.str.replace(combined_pattern, callable) (More complex):")
print(s_replaced_str_callable)
print("-" * 50)


# --- Method 3: Chaining multiple str.replace() calls ---
# Simple but less efficient if you have many replacements.

s_chained = s.copy()
for pattern, replacement in replace_map.items():
    # Apply each replacement sequentially.
    # Be careful with order if replacements could affect subsequent patterns.
    # Also, ensure case sensitivity / regex flags match your needs for each pattern.
    if pattern.startswith('(?i)'): # Handle case-insensitive flag
        actual_pattern = pattern[4:]
        s_chained = s_chained.str.replace(actual_pattern, replacement, case=False, regex=True)
    else:
        s_chained = s_chained.str.replace(pattern, replacement, regex=True)


print("\nMethod 3: Chaining s.str.replace() calls:")
print(s_chained)
print("-" * 50)