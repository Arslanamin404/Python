import DB_connection
import modal
import employee_DAO as emp

# Call the static method without creating an instance
conn = DB_connection.MyConnection.get_connection()
emp_data = emp.Employee_DAO()


def menu():
    print("1. Insert Record")
    print("2. Search Record")
    print("3. View All Records")
    print("4. Delete Record")
    print("5. Exit\n")


def insert():
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ").title()
    emp_dept = input("Enter Department Name: ").upper()
    emp_salary = int(input("Enter Employee Salary: "))

    Emp1 = modal.Employee()
    Emp1.set_id(emp_id)
    Emp1.set_name(emp_name)
    Emp1.set_department(emp_dept)
    Emp1.set_salary(emp_salary)

    emp_data.insert_employee(Emp1)


def search():
    emp_id = int(input("Enter Employee ID to Search: "))
    Emp = emp_data.search_employee(emp_id)
    if Emp is None:
        print("-----------------")
        print("Record Not Found")
        print("-----------------")
    else:
        print("\n-----------------------------------------")
        print(f"EMP-ID: {Emp.get_id()}")
        print(f"Name: {Emp.get_name()}")
        print(f"Department: {Emp.get_department()}")
        print(f"Salary: {Emp.get_salary()}")
        print("-----------------------------------------\n")


def view_all():
    record_list = emp_data.search_all()
    print(f"{len(record_list)} Records Fetched!\n")
    for emp in record_list:
        print(emp.get_id(), end=" ")
        print(emp.get_name(), end=" ")
        print(emp.get_department(), end=" ")
        print(emp.get_salary(), end="\n")


def delete():
    emp_id = int(input("Enter Employee ID to Delete: "))

    Emp = emp_data.search_employee(emp_id)
    if Emp is None:
        print("Record Not Found")
    else:
        print("\n-----------------------------------------")
        print(f"EMP-ID: {Emp.get_id()}")
        print(f"Name: {Emp.get_name()}")
        print(f"Department: {Emp.get_department()}")
        print(f"Salary: {Emp.get_salary()}\n")
        print("-----------------------------------------\n")
        choice = input(
            "Are you sure to delete this record?\n Your Choice [Yes/No]:  ").lower()
        if choice == 'yes':
            emp_data.delete_employee(emp_id)
            print("\nRecord Deleted!")


if __name__ == "__main__":
    menu()
    choice = int(input("Enter you choice: "))

    if choice == 1:
        insert()

    elif choice == 2:
        search()

    elif choice == 3:
        view_all()

    elif choice == 4:
        delete()

    elif choice == 5:
        print("Exiting!")

    else:
        print("Invalid Choice!")
