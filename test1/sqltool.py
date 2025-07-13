# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 08:40:39 2024

@author: HP
"""
import sys
import query
import mysql.connector

# connect to mysql
cnx = mysql.connector.connect(user='root', password='Arpit@10',
                              host='127.0.0.1',
                              database='log')

# Write the query to the database
def write_query_in_database(FINAL_SQL_QUERY):
    
    cursor = cnx.cursor()
    
    query_statment = "INSERT INTO log_query VALUES(%s,CURRENT_TIMESTAMP);"
    cursor.execute(query_statment,(FINAL_SQL_QUERY,))
    
    cnx.commit()
    cursor.close()

# write the query to the file
def write_query_in_file(FINAL_SQL_QUERY,operation):
    timestamp = query.get_current_timestamp()
    
    file_name = operation.replace(" ","_").lower() + "_" + timestamp + ".txt" 
    with open(file_name, "w") as file:
        file.write(FINAL_SQL_QUERY)
    
    file.close()
    print(f'Query is written in - "{file_name}"') 
    
    
print("-" * 10 + " Query Generator Tool " + "-" * 10)
print("Enter operation from below list:")
while True:
    print("1. CREATE DATABASE")
    print("2. CREATE TABLE")
    print("3. INSERT")
    print("4. UPDATE")
    print("5. DELETE")
    print("6. EXIT")

    try:
        operation = int(input("your selection : "))
    except ValueError:
        print("Please select number between 1-6")
        continue
    
    match operation:
        case 1:
            FINAL_SQL_QUERY= query.create_database_query("CREATE DATABASE")
            write_query_in_file(FINAL_SQL_QUERY,"CREATE DATABASE")
        case 2:
            FINAL_SQL_QUERY= query.create_table_query("CREATE TABLE")
            write_query_in_file(FINAL_SQL_QUERY,"CREATE TABLE")
        case 3:
            FINAL_SQL_QUERY= query.insert_query("INSERT")
            write_query_in_file(FINAL_SQL_QUERY,"INSERT")
        case 4:
            FINAL_SQL_QUERY = query.update_query("UPDATE")
            write_query_in_file(FINAL_SQL_QUERY,"UPDATE")
        case 5:
            FINAL_SQL_QUERY = query.delete_query("DELETE")
            write_query_in_file(FINAL_SQL_QUERY,"DELETE")
        case 6:
            sys.exit(0)
        case _:
            print("Enter valid option")

# write query in database    
    write_query_in_database(FINAL_SQL_QUERY)
    
cnx.close()