import sqlite3

# print(sqlite3.sqlite_version)
# connection = sqlite3.connect("test_database.db")
# connection = sqlite3.connect(":memory:")

with sqlite3.connect(":memory:") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now','localtime');"
    results = cursor.execute(query)
    row = results.fetchone()
    print(row[0])

# connection.close()
