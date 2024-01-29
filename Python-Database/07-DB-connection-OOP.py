import MySQLdb
import sys
import time
from msvcrt import getch


class MyDatabase:
    def __init__(self):
        self.__connect()

    def __connect(self):
        try:
            self.__con = MySQLdb.connect(host="localhost",
                                         user="root",
                                         password="futuregen",
                                         database="python_employee_db")
            self.__cursor = self.__con.cursor()
            print("Connected to MySQL Database!\n")
        except MySQLdb.Error as err:
            print(f"An Error has occurred: {str(err)}")

    def __disconnect(self):
        try:
            self.__con.close()
            print("\nConnection Closed!")
        except MySQLdb.Error as err:
            print(
                f"An Error has occurred while closing the connection: {str(err)}")

    def execute_query(self, query, data=None):
        try:
            self.__cursor.execute(query, data)
            self.__con.commit()
            return self.__cursor.fetchall()
        except MySQLdb.Error as err:
            print(f"An Error has occurred: {str(err)}")
        finally:
            self.__disconnect()


class CRUD:
    def __init__(self, database):
        self.database = database

    def insert_record(self):
        emp_name = input("Enter Employee Name: ").title()
        emp_dept = input("Enter Employee Department: ").upper()
        emp_salary = int(input("Enter Employee Salary: "))

        query = "INSERT INTO employees (employee_name, department, salary) VALUES (%s, %s, %s)"
        data = (emp_name, emp_dept, emp_salary)
        self.database.execute_query(query, data)
        print("\nEmployee Record Inserted Successfully.\n")

        print("Press Any Key To Continue...")
        getch()

    def view_records(self):
        query = "SELECT * FROM employees"
        rows = self.database.execute_query(query)
        print("-----------------------------------------------------------------")
        print(f"{'Emp-ID':<15}{'NAME':<20}{'DEPARTMENT':<20}{'SALARY'}")
        print("-----------------------------------------------------------------")
        for row in rows:
            print(f"{row[0]:<10}{row[1]:<25}{row[2]:<20}{row[3]}")
        print("-----------------------------------------------------------------")
        print("\nPress Any Key To Continue...")
        getch()

    def search_employee(self):
        emp_id = int(input("Enter Employee ID to Search: "))
        query = "SELECT * FROM employees WHERE id = %s"
        data = (emp_id,)
        result = self.database.execute_query(query, data)
        if result:
            for row in result:
                print(f"Employee ID: {row[0]}")
                print(f"Employee Name: {row[1]}")
                print(f"Employee Department: {row[2]}")
                print(f"Employee Salary: {row[3]}")
        else:
            print("\nRecord Not Found!")
        print("\nPress Any Key To Continue...")
        getch()

    def delete_employee(self):
        emp_id = int(input("Enter Employee ID to Delete: "))
        query = "DELETE FROM employees WHERE id = %s"
        data = (emp_id,)
        self.database.execute_query(query, data)
        print("Employee Record Deleted Successfully.")
        print("Press Any Key To Continue...")
        getch()


def main():
    while True:
        print("\n\t\t#########################################################")
        print("\t\t\tWelcome to the Employee Management System")
        print("\t\t#########################################################\n")
        print("Please Select An Action --->\n")
        print("1. Insert Employee Record\n2. View All Records\n3. Search Employee Record\n4. Delete Employee Record\n5. Exit\n")
        try:
            user_choice = int(input("Enter Your Choice [1/2/3/4/5]: "))
            myDB = MyDatabase()
            curd = CRUD(myDB)
            if user_choice == 1:
                curd.insert_record()
            elif user_choice == 2:
                curd.view_records()
            elif user_choice == 3:
                curd.search_employee()
            elif user_choice == 4:
                curd.delete_employee()
            elif user_choice == 5:
                print("Exiting...")
                time.sleep(1)
                sys.exit()
            else:
                print("Invalid Choice. Please Enter [1/2/3/4/5]")
                print("Press Any Key To Continue...")
                getch()
        except ValueError:
            print("Error! Please Enter a Valid Integer Input [1/2/3/4/5]")
            sys.exit()


if __name__ == "__main__":
    main()
