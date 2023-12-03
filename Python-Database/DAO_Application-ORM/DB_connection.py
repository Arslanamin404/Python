import MySQLdb


class MyConnection:
    @staticmethod
    def get_connection():
        try:
            con = MySQLdb.connect(host="localhost",
                                  user="root",
                                  password="futuregen",
                                  database="python_employee_db")
            return con
        except MySQLdb.Error as err:
            print(f"An Error Has Occurred: {err}")
