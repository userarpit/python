# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:40:46 2024

@author: HP
"""
import datetime
import time


def create_database_query(operation_string):
    database_name = input("Enter database name - ").upper()
    FINAL_SQL_QUERY = " ".join([operation_string,database_name])
    return FINAL_SQL_QUERY
    
def create_table_query(operation_string):
    table_name = input("Enter table name - ").upper()
    FINAL_SQL_QUERY =""
    SQL_QUERY = " ".join([operation_string, table_name, "(\n"])
    
    file = input("Enter name of the text file for column name, column type, column length, separated by comma - ")
    
    f = open(file, "r")
    for line in f:
        line = line.strip()
        line_list = line.split(",")
        
        SQL_QUERY = SQL_QUERY + "    " + line_list[0] + " " + line_list[1]
        SQL_QUERY = SQL_QUERY + "(" + line_list[2] + "),\n" if len(line_list) > 2 else SQL_QUERY + ",\n"       
    
    SQL_QUERY = SQL_QUERY[:-2]
    f.close()
    SQL_QUERY = SQL_QUERY + "\n);"
    
    FINAL_SQL_QUERY = SQL_QUERY
    return FINAL_SQL_QUERY

def insert_query(operation_string):
    table_name = input("Enter table name - ").upper()
    FINAL_SQL_QUERY =""

    
    file = input("Enter name of the text file for INSERT columns, INSERT values - ")
    f = open(file, "r")
    
    # extract header
    header = f.readline().strip()
    header = list(header.split(","))
    for line in f:
        line = line.strip()
        SQL_QUERY = " ".join([operation_string, "INTO " + table_name, "("])
        SQL_QUERY = SQL_QUERY + ",".join(header)
        SQL_QUERY = SQL_QUERY + ")\n"
        SQL_QUERY = SQL_QUERY + " VALUES ("
        
        
    # add VALUES CLAUSE    
        
        line_list = list(line.split(","))
        
        for i in range(len(line_list)):
            
            try:
                int(line_list[i])
            except ValueError:
                SQL_QUERY = SQL_QUERY + '"' + line_list[i] + '",'
            else:
                SQL_QUERY = SQL_QUERY + line_list[i] + ","
       
        SQL_QUERY = SQL_QUERY[:-1]           
        SQL_QUERY = SQL_QUERY + ");\n"
  
  
        FINAL_SQL_QUERY = FINAL_SQL_QUERY + SQL_QUERY
     
    f.close()
    return FINAL_SQL_QUERY

def update_query(operation_string):
    table_name = input("Enter table name - ").upper()
    
    file = input("Enter name of the text file for SET columns, WHERE condition, and their values - ")
    f = open(file, "r")
    
    set_column = list(map(int,input("Enter the number of the columns, for SET clause, separated by comma - ").split(",")))
    where_column = list(map(int,input("Enter the number of the columns, for WHERE condition, separated by comma - ").split(",")))
    
    # extract header
    header = f.readline().strip()
    header = list(header.split(","))
    FINAL_SQL_QUERY = ""
    
    for line in f:
    
        SQL_QUERY = " ".join([operation_string, table_name])  
        SQL_QUERY = SQL_QUERY + "\n"
        
    # add SET CLAUSE    
        
        line_list = list(line.split(","))
        try:
            int(line_list[set_column[0]-1])
        except ValueError:
            SQL_QUERY = SQL_QUERY + " ".join(["   SET",
                                          header[set_column[0]-1] + " =",
                                          '"' + line_list[set_column[0]-1].strip() + '"\n']) 
        else:
            SQL_QUERY = SQL_QUERY + " ".join(["   SET",
                                          header[set_column[0]-1] + " =",
                                          line_list[set_column[0]-1].strip() + "\n"])
            
        for set_column_range in range(1,len(set_column)):
            try:
                int(line_list[set_column[set_column_range]-1].strip())
            except ValueError:
                SQL_QUERY = SQL_QUERY + " ".join(["     ,",
                                              header[set_column[set_column_range]-1] + " =",
                                              '"' + line_list[set_column[set_column_range]-1].strip() + '"\n'])
            else:
                SQL_QUERY = SQL_QUERY + " ".join(["     ,",
                                              header[set_column[set_column_range]-1] + " =",
                                              line_list[set_column[set_column_range]-1].strip() + '\n'])
    # add WHERE condition
        try:
            int(line_list[where_column[0]-1])
        except ValueError:
            SQL_QUERY = SQL_QUERY + " ".join([" WHERE",
                                          header[where_column[0]-1] + " =",
                                          '"' + line_list[where_column[0]-1].strip() + '"\n']) 
        else:
            SQL_QUERY = SQL_QUERY + " ".join([" WHERE",
                                          header[where_column[0]-1] + " =",
                                          line_list[where_column[0]-1].strip() + "\n"])
            
        for where_column_range in range(1,len(where_column)):
            try:
                int(line_list[where_column[where_column_range]-1].strip())
            except ValueError:
                SQL_QUERY = SQL_QUERY + " ".join(["   AND",
                                              header[where_column[where_column_range]-1] + " =",
                                              '"' + line_list[where_column[where_column_range]-1].strip() + '"\n'])
            else:
                SQL_QUERY = SQL_QUERY + " ".join(["   AND",
                                              header[where_column[where_column_range]-1] + " =",
                                              line_list[where_column[where_column_range]-1].strip() + '\n'])
        
        SQL_QUERY = SQL_QUERY + ";\n"
        FINAL_SQL_QUERY = FINAL_SQL_QUERY + SQL_QUERY
    
    f.close()        
    return FINAL_SQL_QUERY

def delete_query(operation_string):
    
    table_name = input("Enter table name - ").upper()
    FINAL_SQL_QUERY =""

    file = input("Enter name of the text file for DELETE column names and values - ")
    f = open(file, "r")
    SQL_QUERY = " ".join([operation_string,"FROM",table_name,"\n"])
    SQL_QUERY = SQL_QUERY + " WHERE "
    first_line = f.readline().strip()
    first_line_list = list(first_line.split(","))
    
    SQL_QUERY = SQL_QUERY + first_line_list[0] + "=" 
    SQL_QUERY = verify_value_and_add_delete(SQL_QUERY,first_line_list[1])
        
    for line in f:
        line=line.strip()
        line_list=list(line.split(","))
        
        SQL_QUERY = SQL_QUERY + "   AND " + line_list[0] + "=" 
        SQL_QUERY = verify_value_and_add_delete(SQL_QUERY,line_list[1])
        FINAL_SQL_QUERY = FINAL_SQL_QUERY + SQL_QUERY 
        
    FINAL_SQL_QUERY = FINAL_SQL_QUERY + ";"
    
    f.close()
    
    return FINAL_SQL_QUERY
    
def verify_value_and_add_delete(SQL_QUERY,value):
    try:
        int(value)
    except ValueError:
        SQL_QUERY = SQL_QUERY + '"' + value + '"\n'
    else:
        SQL_QUERY = SQL_QUERY + value + '\n'
        
    return SQL_QUERY

def get_current_timestamp():
    current_timestamp = time.time()

    timestamp = current_timestamp  # Example timestamp
    datetime_object = datetime.datetime.fromtimestamp(timestamp)

    datetime_object = str(datetime_object)
    datetime_object = datetime_object.replace(":","_")
    datetime_object = datetime_object.replace(".","_")
    datetime_object = datetime_object.replace("-","_")
    datetime_object = datetime_object.replace(" ","_")
    return datetime_object
