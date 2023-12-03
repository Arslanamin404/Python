import MySQLdb
try:
    # connection establish
    con = MySQLdb.connect(host="localhost",
                          user="root",
                          password="futuregen",
                          database="python_employee_db")
    print("Connected to MYSQL Database successfully!\n")
    
    # query execution
    emp_ID = int(input("Enter Employee ID to Delete: "))
    query = "SELECT * FROM employees WHERE id = %d" #parameterized Query
    cursor = con.cursor()
    cursor.execute(query % emp_ID)
    row = cursor.fetchone()
    
    if (cursor.rowcount == 0):
        print(f"\nNo Record Found with Employee ID = {emp_ID}\n")
    else:
        print("\nRecord Found:\n--------------------------")
        print("Employee ID: %d \nEmployee Name: %s \nDepartment: %s \nSalary: %d" % (row[0], row[1], row[2], row[3]))
        print("----------------------------\n")
        
        choice = int(input("Are You sure you want to delete this record?\nEnter 0 for NO and 1 for YES : "))
        if choice:
            query = "DELETE FROM employees WHERE id = %d"
            cursor.execute(query%emp_ID)
            con.commit()
            print("\nRecord Deleted Successfully!\n")
        else:
            print("\nNo worries! Your data is safe.\n")
except ValueError:
    print("\aERROR: Invalid Input! Please enter a valid integer value for Employee ID.\n")
except MySQLdb.Error as err:
    print(f"An Error has Occurred: {err}")
finally:
    con.close()
    print("Connection Closed!\n")
