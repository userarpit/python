import pandas as pd
from io import StringIO
# This URL is just an example; replace with a real one if needed
url = 'https://example.com/data.html' # Replace with a URL that has tables with IDs/classes

# To simulate, let's use an HTML string with a specific ID
html_with_id = """
<table id="ignoreThis">
  <tr><td>1</td></tr>
</table>
<table id="targetTable" class="important-data">
  <tr><th>Header A</th><th>Header B</th></tr>
  <tr><td>Value 1</td><td>Value 2</td></tr>
</table>
"""

try:
    # Target the table with id="targetTable"
    df_attrs_id = pd.read_html(StringIO(html_with_id), attrs={'id': 'targetTable'})[0]
    print("\nDataFrame targeted by ID:\n", df_attrs_id)

    # Target the table with class="important-data"
    df_attrs_class = pd.read_html(StringIO(html_with_id), attrs={'class': 'important-data'})[0]
    print("\nDataFrame targeted by Class:\n", df_attrs_class)

except Exception as e:
    print(f"Could not read HTML (example): {e}")

# If you're reading from a live URL, errors like 403 (Forbidden) are common.
# In such cases, you might need to use the `requests` library to fetch the HTML
# with appropriate headers (like a User-Agent) and then pass the text to read_html.
# import requests
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     df_from_request = pd.read_html(response.text, attrs={'id': 'myDataTable'})[0]
#     print(df_from_request)
# else:
#     print(f"Failed to fetch URL: {response.status_code}")