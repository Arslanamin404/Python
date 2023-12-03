import MySQLdb
from tkinter import messagebox


class IMSDataBase:
    def __init__(self):
        self.__connect()
        self.__create_table()

    def __connect(self):
        try:
            self.__con = MySQLdb.connect(host="localhost",
                                         user="root",
                                         password="futuregen",
                                         database="inventory_management_system")
            self.__cursor = self.__con.cursor()
        except MySQLdb.Error as err:
            print(f"An Error Has Occurred: {err}")
            messagebox.showerror("Error", f"An Error Has Occurred: {err}")

    def execute_query(self, query, data=None):
        try:
            self.__connect()
            self.__cursor.execute(query, data)
            self.__con.commit()
            self.__disconnect()
            return self.__cursor.fetchall()
        except MySQLdb.Error as err:
            print(f"An Error Has Occurred: {err}")
            messagebox.showerror("Error", f"An Error Has Occurred: {err}")

    def __disconnect(self):
        try:
            self.__con.close()
        except MySQLdb.Error as err:
            print(f"An Error Has Occurred: {err}")
            messagebox.showerror("Error", f"An Error Has Occurred: {err}")

    def __create_table(self):
        create_employee_table_query = "CREATE TABLE IF NOT EXISTS employee(emp_id INT AUTO_INCREMENT PRIMARY KEY,name  VARCHAR(150) NOT NULL,email VARCHAR(100) UNIQUE NOT NULL,gender VARCHAR(15) NOT NULL,contact VARCHAR(20) NOT NULL,dob VARCHAR(50) NOT NULL,doj VARCHAR(50) NOT NULL,password VARCHAR(50) NOT NULL,utype VARCHAR(50) NOT NULL,address VARCHAR(250) NOT NULL,salary INT NOT NULL)"
        self.execute_query(create_employee_table_query)

        create_supplier_table_query = "CREATE TABLE IF NOT EXISTS supplier(invoice INT AUTO_INCREMENT PRIMARY KEY,name  VARCHAR(150) NOT NULL,contact VARCHAR(50) UNIQUE NOT NULL,description TEXT NOT NULL)"
        self.execute_query(create_supplier_table_query)


if __name__ == "__main__":
    IMSdb = IMSDataBase()
