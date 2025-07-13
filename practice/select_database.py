import sqlite3

select = """ select * from People """
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    # cursor.execute(create_table)
    cursor.execute(select)
    rows = cursor.fetchall()

for row in rows:
    print(row)
