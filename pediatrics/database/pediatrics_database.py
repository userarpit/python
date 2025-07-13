import psycopg2

def connect():
    conn = psycopg2.connect(database = "postgres", 
                                user = "postgres", 
                                host= 'localhost',
                                password = "Arpit@10",
                                port = 5432)

            # Open a cursor to perform database operations
    cur = conn.cursor()
        
    return conn, cur

def close(conn,cur):
    # Make the changes to the database persistent
    # conn.commit()
    # Close cursor and communication with the database
        if conn:
            cur.close()
            conn.close()

def update_database(first_name,last_name,gender,dob,final_data):
    try:
        conn, cur = connect()
        
        query = '''INSERT INTO pediatrics.immunization_schedule (first_name,last_name,gender,date_of_birth,given_value,given_on,weight,height,drug_name,batch_no,mfg_date,expiry_date,any_comments) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        ON CONFLICT (first_name, last_name, gender, date_of_birth, given_value) DO UPDATE 
        SET (given_value,given_on,weight,height,drug_name,batch_no,mfg_date,expiry_date,any_comments) = 
        (EXCLUDED.given_value,EXCLUDED.given_on,EXCLUDED.weight,EXCLUDED.height,EXCLUDED.drug_name,EXCLUDED.batch_no,EXCLUDED.mfg_date,EXCLUDED.expiry_date,EXCLUDED.any_comments);'''
        # print(query)
        for data in final_data:
              
            cur.execute(query,(first_name.capitalize(),last_name.capitalize(),gender,dob,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
            conn.commit()
    
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data to PostgreSQL", error)

    finally:
        close(conn,cur)

def search(first_name,last_name,gender,dob):
    
    # connect to postgres
    try:
        conn, cur = connect()

        # Execute a command: create datacamp_courses table
        query = '''SELECT A.age, A.vaccines, B.given_on, B.weight, B.height, B.drug_name, B.batch_no, B.mfg_date, B.expiry_date, B.any_comments FROM pediatrics.vaccines as A, pediatrics.immunization_schedule as B
                    WHERE LOWER(B.first_name) = %s
                    AND LOWER(B.last_name) = %s
                    AND B.gender = %s
                    AND B.date_of_birth = %s
                    AND A.reference_number = B.given_value;'''
        
        cur.execute(query, (first_name.lower(),last_name.lower(),gender,dob))
        rows=cur.fetchall()
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        close(conn,cur)

    return rows
def get_number_of_row_vaccines():
    # connect to postgres
    try:
        conn, cur = connect()

        # Execute a command: create datacamp_courses table
        query = '''SELECT count(*) FROM pediatrics.vaccines as A'''
        
        cur.execute(query)
        count=cur.fetchone()
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        close(conn,cur)

    return count
    
def get_vaccines_table():
    try:
        conn, cur = connect()
        # Execute a command: create datacamp_courses table
        query = '''SELECT A.age, A.vaccines FROM pediatrics.vaccines as A order by A.reference_number asc;'''
        
        cur.execute(query)
        rows=cur.fetchall()
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        close(conn,cur)

    return rows

def add_new_baby_row(*args):
    try:
        conn, cur = connect()
        query = '''INSERT INTO pediatrics.baby VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        # print(query)
        cur.execute(query,(args[0].capitalize(),args[1].capitalize(),args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],args[11],args[12],args[13],args[14],args[15],args[16],args[17]))
    
        conn.commit()
    
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data to PostgreSQL", error)

    finally:
        close(conn,cur)

def baby_found(first_name,last_name,gender,dob):
    try:
        
        conn, cur = connect()
        query = '''SELECT * FROM pediatrics.baby as A
                    WHERE LOWER(A.first_name) = %s
                    AND LOWER(A.last_name) = %s
                    AND A.gender = %s
                    AND A.date_of_birth = %s
        '''
        # print(query)
        cur.execute(query,(first_name.lower(),last_name.lower(),gender,dob))
    
        if cur.rowcount > 0:
            return True
        else:
            return False
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        close(conn,cur)

if __name__ == "__main__":
    search()