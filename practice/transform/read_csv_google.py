import pandas as pd
# https://docs.google.com/spreadsheets/d/1V3qBhVhVZWaOR1sLxbBccwKLDzQsBDuAvYHXwa1wXdU/edit?usp=sharing
file_id = "1V3qBhVhVZWaOR1sLxbBccwKLDzQsBDuAvYHXwa1wXdU"
google_drive_url = "https://docs.google.com/spreadsheets/d/1V3qBhVhVZWaOR1sLxbBccwKLDzQsBDuAvYHXwa1wXdU/edit?usp=sharing"


try:

    print(f"Attempting to read CSV from Google Drive URL: {google_drive_url}")

        # Use pandas.read_csv to read the file directly from the URL.
        # It handles the HTTP request and parsing automatically.
    df = pd.read_csv(google_drive_url)

    print("Successfully loaded DataFrame from Google Drive!")
        # return df
    print(df)

except pd.errors.EmptyDataError:
    print(f"Error: The CSV file associated with ID '{file_id}' is empty.")
        # return pd.DataFrame() # Return an empty DataFrame
except pd.errors.ParserError as pe:
    print(f"Error parsing the CSV file. Check delimiter, header, or file format: {pe}")
        # return None
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print("Please ensure the following:")
    print(f"1. The provided Google Drive File ID '{file_id}' is correct.")
    print("2. The Google Drive file's sharing settings are set to 'Anyone with the link can view'.")
    print("3. The file is indeed a valid CSV file.")
    print("4. Your internet connection is stable.")
    # return None