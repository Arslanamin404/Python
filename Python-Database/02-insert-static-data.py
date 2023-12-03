import MySQLdb

try:
    con = MySQLdb.connect(host="localhost",
                          user="root",
                          password="futuregen",
                          database="python_employee_db")
    print("Connected to MYSQL Successfully!\n")

    query = """INSERT INTO users (username,email) VALUES
              ('Admin', 'futuregen.jk@gmail.com'),
              ('Muneeb Inayat', 'muneebinayat69@gmail.com'),
              ('Sheezan Firdous', 'lonesheezan72@gmail.com'),
              ('Zain Zahoor', 'zainzahoor116@gmail.com'),
              ('Mohammad Arsalan Rather', 'arslanamin.org@gmail.com')
              """

    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    print("Record Inserted Successfully!")
except MySQLdb.Error as err:
    print(f"Error! Something unexpected occurred: {err}")
finally:
    con.close()
