import sqlite3

sql = """
drop table if exists People;
CREATE TABLE PEOPLE(Firstname TEXT, Lastname TEXT, Age INT);
"""
people_values = (
    ("Arpit", "Khandelwal", 38),
    ("Garvit", "Khandelwal", 37),
    ("Shanaya", "Khandelwal", 13),
)

insert_query = """
INSERT INTO PEOPLE values(?, ?, ?); 
"""

select_query = """
select * from people where age < 30;"""

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(sql)
    cursor.executemany(insert_query, people_values)
    cursor.execute(select_query)
    rows = cursor.fetchall()


for row in rows:
    print(row)
