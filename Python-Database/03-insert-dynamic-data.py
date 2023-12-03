import MySQLdb
try:
    # connection
    con = MySQLdb.connect(host="localhost",
                          user="root",
                          password="futuregen",
                          database="python_employee_db")
    print("Connected to MYSQL Successfully!\n")
    nun_employees = int(
        input("Number of Employees to be Inserted in DataBase: "))
    for i in range(nun_employees):
        # userInput
        print("\n-----------------------------------")
        print(f"Details of Employee: {i+1}")
        print("-----------------------------------")
        name = input("Enter Employee Name: ").title()
        department = input("Enter Department: ").upper()
        salary = int(input("Enter Employee Salary: "))

        data = (name, department, salary)
        query = f"INSERT INTO employees (employee_name,department,salary) VALUES('%s','%s',%d)"

        # query execution
        cursor = con.cursor()
        cursor.execute(query % data)
        con.commit()
        print(f"\n{cursor.rowcount} Record Inserted Successfully!\n")

# handling exceptions
except ValueError:
    print("ERROR! Please Enter a Valid Input.")
except MySQLdb.Error as err:
    print(f"An Error has occurred: {err}.")

# closing connection
finally:
    con.close()
    print("Connection Closed!")
