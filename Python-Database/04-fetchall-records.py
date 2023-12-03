import MySQLdb
try:
    con = MySQLdb.connect(host="localhost",
                          user="root",
                          password="futuregen",
                          database="python_employee_db")
    print("Connect to MYSQL Successfully!\n")
    query = "SELECT * FROM employees"
    cursor = con.cursor()
    cursor.execute(query)
    # result contains all the data of table(row,col)
    result = cursor.fetchall()
    print("------------------------------------------------------------------------------------")
    print(f"{'  ID':30} {'NAME':15} {'DEPARTMENT':25} SALARY")
    for row in result:
        # print formatted data
        print("------------------------------------------------------------------------------------")
        print("%5d %30s %20s %20d" % (row[0], row[1], row[2], row[3]))
        # print data without formatting
        # print(row)
    print("------------------------------------------------------------------------------------")
    
    print(f"\n{cursor.rowcount} records fetched!\n")
except MySQLdb.Error as err:
    print(f"An Error has occurred: {err}")
finally:
    con.close()
    print("Connection Closed!")
