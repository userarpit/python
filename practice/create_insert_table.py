import sqlite3

create_table = """
CREATE TABLE PEOPLE(Firstname TEXT, Lastname TEXT, Age INT)"""

insert_row = """
insert into PEOPLE values('Ron','Obvious',42)"""

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    # cursor.execute(create_table)
    cursor.execute(insert_row)

