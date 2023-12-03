import MySQLdb
try:
    con = MySQLdb.connect(host="localhost",
                          user="root",
                          password="futuregen",
                          database="python_employee_db"
                          )
    print("Connected to MySQL Successfully!")

    query = """CREATE TABLE users (
                id INT PRIMARY KEY NOT NULL,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
                );"""

    # cursor object
    cursor = con.cursor()
    # execute the SQL query
    cursor.execute(query)
    # commit the changes
    con.commit()
except MySQLdb.Error as err:
    print(f"Error! Something unexpected occurred: {err}")
finally:
    con.close()
