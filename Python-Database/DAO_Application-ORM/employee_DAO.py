import DB_connection as db_conn
import modal


class Employee_DAO:
    def __init__(self):
        try:
            self.__con = db_conn.MyConnection.get_connection()
            print("\n---------------------\nConnected to MySQL!\n---------------------\n")
            self.__cursor = self.__con.cursor()
        except Exception as err:
            print(f"An Error Has Occurred: {err}")

    def insert_employee(self, emp):
        try:
            query = "INSERT INTO employees (id, employee_name, department, salary) VALUES (%s, %s, %s, %s)"
            data = (emp.get_id(), emp.get_name(),
                    emp.get_department(), emp.get_salary())
            self.__cursor.execute(query, data)
            self.__con.commit()
            print("\n----------------------------\nRecord Inserted Successfully!\n----------------------------\n")
        except Exception as err:
            print(f"An Error Has Occurred: {err}")

    def search_all(self):
        employee_list = []
        try:
            query = "SELECT * FROM employees"
            self.__cursor.execute(query)
            result = self.__cursor.fetchall()
            for row in result:
                E1 = modal.Employee()
                E1.set_id(row[0])
                E1.set_name(row[1])
                E1.set_department(row[2])
                E1.set_salary(row[3])
                
                employee_list.append(E1)
            return employee_list
        except Exception as err:
            print(f"An Error Occurred : {err}")

    def search_employee(self, emp_id):
        try:
            query = "SELECT * FROM employees WHERE id = %d"
            self.__cursor.execute(query % emp_id)
            result = self.__cursor.fetchone()
            if result is None:
                return None
            else:
                E1 = modal.Employee()
                E1.set_id(result[0])
                E1.set_name(result[1])
                E1.set_department(result[2])
                E1.set_salary(result[3])
                return E1
        except Exception as err:
            print(f"An Error Has Occurred: {err}")
            
    def delete_employee(self,emp_id):
        try:
            query = "DELETE FROM employees WHERE id = %d"
            self.__cursor.execute(query % emp_id)
            self.__con.commit()
        except Exception as err:
            print(f"An Error Has Occurred: {err}")
        

    def __del__(self):
        try:
            self.__con.close()
            print("\n----------------------------\nConnection Closed!\n----------------------------\n")
        except Exception as err:
            print(f"An Error Has Occurred: {err}")