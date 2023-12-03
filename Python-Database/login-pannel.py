import MySQLdb


class MyDatabase:
    def __init__(self):
        self.__connect()

    def __connect(self):
        try:
            self.__con = MySQLdb.connect(
                host="localhost", user="root", password="futuregen", database="python_employee_db")

            print("Connect to MySQL DataBase!\n")
            self.__cursor = self.__con.cursor()
        except MySQLdb.Error as err:
            print("An Error Has Occurred", str(err))

    def __disconnect(self):
        try:
            self.__con.close()
            print("\nConnection Closed!")
        except MySQLdb.Error as err:
            print("An Error Has Occurred", str(err))

    def register_user(self, f_name, l_name, username, password):
        try:
            query = "SELECT * FROM login WHERE username = %s"
            self.__cursor.execute(query, (username,))
            user = self.__cursor.fetchone()
            if user:
                print(
                    "\n----------------------------------------------------------------------------------------")
                print("User Already Exist",
                      "Username already taken. Please choose a different username.")
                print(
                    "----------------------------------------------------------------------------------------")

            else:
                new_query = "INSERT INTO login (first_name, last_name, username, password) VALUES (%s, %s, %s, %s)"
                data = (f_name, l_name, username, password)
                self.__cursor.execute(new_query, data)
                print("\n--------------------------------------------")
                print("Success! User Registered Successfully!")
                print("--------------------------------------------")
                self.__con.commit()
        except MySQLdb.Error as err:
            print("\n--------------------------------------------------")
            print("An Error Occurred", str(err))
            print("--------------------------------------------------")

        finally:
            self.__disconnect()

    def login_user(self, username, password):
        try:
            query = "SELECT * FROM login WHERE username = %s AND password = %s"
            data = (username, password)
            self.__cursor.execute(query, data)  # Replace % with a comma
            user = self.__cursor.fetchone()

            if user:
                print("\n----------------------------")
                print("Login Successful!")
                print("----------------------------\n")
            else:
                print("\n----------------------------")
                print("Invalid Username or Password")
                print("----------------------------\n")
        except MySQLdb.Error as err:
            print(f"An Error Occurred: {str(err)}")
        finally:
            self.__disconnect()

    def execute_query(self):
        try:
            query = "SELECT * From login"
            self.__cursor.execute(query)
            rows = self.__cursor.fetchall()
            # dont print password
            print("-----------------------------------------------------------------------------------------------------------")            
            print(f"{'Emp-ID':28}{'FIRST NAME':30}{'LAST NAME':32}{'USERNAME'}")
            print("-----------------------------------------------------------------------------------------------------------")            
            for row in rows:
                print("%5d %30s %30s %30s"%(row[0],row[1],row[2],row[3]))
                print("-----------------------------------------------------------------------------------------------------------")            
        except MySQLdb.Error as err:
            print(f"An Error Occurred: {str(err)}")
        finally:
            self.__disconnect()


def menu():
    print("Employee Login Panel\n")
    print("1. Register")
    print("2. Login")
    print("3. View Registered Users")
    print("4. Exit\n")


if __name__ == "__main__":
    db = MyDatabase()
    menu()
    choice = int(input("Please Enter your choice: "))

    if choice == 1:
        first_name = input("Please Enter Your First Name: ").title()
        last_name = input("Please Enter Your Last Name: ").title()
        username = input("Please Enter Your Username: ").lower()
        password = input("Please Enter Your Password: ")
        db.register_user(first_name, last_name, username, password)
    elif choice == 2:
        username = input("Please Enter Your Username: ").lower()
        password = input("Please Enter Your Password: ")
        db.login_user(username, password)

    elif choice == 3:
        admin_id = "futuregen"
        admin_pw = "error404"
        print("#################################################################################################################")
        print("\t\t\t\t\tADMIN PANEL")
        print("#################################################################################################################\n")
        ad_id = input("Enter Admin ID: ")
        ad_paswd = input("Enter Admin Password: ")
        try:
            if ad_id or ad_paswd:
                if ad_id == admin_id and ad_paswd == ad_paswd:
                    print(
                        "\n****************************************************************************************************************")
                    print("\t\t\t\t\tWelcome To ADMIN SIDE")
                    print("****************************************************************************************************************\n")
                    db.execute_query()
                else:
                    print("\nInvalid ID or Password")
            else:
                print("\nPlease Enter All Required Fields: ")
        except ValueError:
            print("\nError! Please enter a valid Input.")
        except Exception as err:
            print(f"\nERROR! Something unexpected has occurred: {err}")

    elif choice == 4:
        print("Exiting. . .")

    else:
        print("Invalid Choice. . .")
