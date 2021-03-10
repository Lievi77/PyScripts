import psycopg2


def connect_to_group_db():
    
    #postgres connection data
    conn = psycopg2.connect(

        host = "eecs.uottawa.ca",
        database = "group_4",
        user = "lguzm038",
        password = "Kyorzkyre77!",
        port= 15432
    )

    cur = conn.cursor()

    
    with open('filtered_patients.csv', 'r') as f:
        next(f) #skip headers
        cur.copy_from(f, 'fds_project.patient_dim', sep = ',')
    
    conn.commit()


    #test_query = "ALTER TABLE fds_project.patient_dim ALTER COLUMN gender type VARCHAR(20)"

    #cur.execute(test_query)

    #conn.commit()

    #after each execute, commit with cur.commit

    # print(version)

    #good practice to close the connection
    cur.close()



def upload_data():
    connect_to_group_db()


upload_data()
