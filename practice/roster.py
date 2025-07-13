import sqlite3

sql_query = """
drop table if exists roster;
create table roster (
    Name TEXT,
    Species TEXT,
    Age INT);
"""
insert_values = (
    ('Benjamin Sisko', 'Bajoran', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
)
# select_query = "SELECT * FROM ROSTER;"
select_bajoran = "select * from roster where species = 'Bajoran';"

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(sql_query)
    cursor.executemany("INSERT INTO ROSTER VALUES(?, ?, ?);", insert_values)

    cursor.execute("UPDATE ROSTER SET Name = ? WHERE Name = 'Jadzia Dax'", ('Ezri Dax',))
    # cursor.execute(select_query)
    # rows = cursor.fetchall()

    cursor.execute(select_bajoran)
    bajoran_rows = cursor.fetchall()

# for row in rows:
#     print(row)

for row in bajoran_rows:
    print(row)
