from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import MySQLdb

# Database Class


class MyDatabase:
    def __init__(self):
        self.__connect()

    # Connection Method
    def __connect(self):
        try:
            self.__con = MySQLdb.connect(host="localhost",
                                         user="root",
                                         password="futuregen",
                                         database="python_employee_db")
            print("Connect to MySQL DataBase!\n")
            self.__cursor = self.__con.cursor()

        except MySQLdb.Error as err:
            print(f"An Error has occurred: {str(err)}")

    # query Execution Method
    def execute_query(self, query, data=None):
        try:
            self.__cursor.execute(query, data)
            self.__con.commit()
            self.__disconnect()
            return self.__cursor.fetchall()
        except MySQLdb.Error as err:
            messagebox.showerror("An Error Occurred", str(err))
            print(f"An Error Occurred: {str(err)}")

    # Search Method
    def search_query(self, query, emp_id):
        try:
            self.__cursor.execute(query % emp_id)
            self.__disconnect()
            return self.__cursor.fetchone()
        except MySQLdb.Error as err:
            messagebox.showerror("An Error Occurred", str(err))
            print(f"An Error Occurred: {str(err)}")

    # Disconnection Method
    def __disconnect(self):
        try:
            self.__con.close()
            print("\nConnection Closed!")
        except MySQLdb.Error as err:
            print(
                f"An Error has occurred while closing the connection: {str(err)}")


class MainFrame(MyDatabase):
    # constructor
    def __init__(self, window, db):
        self.window = window
        self.db = db

        self.window.geometry("1500x700+10+40")
        self.window.iconbitmap("recruitment_icon.ico")
        self.window.title(
            "Employee Management System | Developed By Mohammad Arsalan Rather")
        self.window.config(bg="#1b1b1b")

        # Frame heading
        self.head_icon = PhotoImage(file="recruitment.png")
        self.head_label = Label(self.window, image=self.head_icon, compound=LEFT,
                                text="Employee Management System",
                                font=("Times New Roman", 40, "bold"),
                                bg="#1b1b55", fg="#39FF14", padx=20, height=20)
        self.head_label.place(x=0, y=0, relwidth=1, height=70)

        # create Frame
        self.frame = Frame(self.window, bd=3, relief=RIDGE,
                           width=1000, height=500, bg="#1b1b1b")
        self.frame.propagate(0)
        self.frame.place(x=250, y=100)

        # vars
        self.emp_id = IntVar()
        self.emp_name = StringVar()
        self.emp_dept = StringVar()
        self.emp_salary = IntVar()

        # ID-label/Entry
        self.id_label = Label(self.frame, text="Employee ID ",
                              font=("Arial", 18, "bold"),
                              bg="#1b1b1b", fg="white")
        self.id_label.place(x=150, y=50)
        self.id_entry = Entry(self.frame, width=20,
                              textvariable=self.emp_id, font=("Arial", 18, "bold"), fg="blue")
        self.id_entry.place(x=310, y=50)

        # NAME-label/Entry
        self.name_label = Label(self.frame,
                                text="Employee NAME ",
                                font=("Arial", 18, "bold"),
                                bg="#1b1b1b", fg="white")
        self.name_label.place(x=150, y=120)
        self.name_entry = Entry(self.frame, width=40,
                                textvariable=self.emp_name, font=("Arial", 18, "bold"), fg="blue")
        self.name_entry.place(x=360, y=120)

        # Department-label/Entry
        self.dept_label = Label(self.frame, text="Employee DEPARTMENT ",
                                font=("Arial", 18, "bold"),
                                bg="#1b1b1b", fg="white")
        self.dept_label.place(x=150, y=190)
        self.dept_entry = Entry(self.frame, width=20,
                                textvariable=self.emp_dept, font=("Arial", 18, "bold"), fg="blue")
        self.dept_entry.place(x=455, y=190)

        # SALARY-label/Entry
        self.salary_label = Label(self.frame,
                                  text="Employee SALARY ",
                                  font=("Arial", 18, "bold"), bg="#1b1b1b", fg="white")
        self.salary_label.place(x=150, y=260)
        self.salary_entry = Entry(self.frame, width=20,
                                  textvariable=self.emp_salary, font=("Arial", 18, "bold"), fg="blue")
        self.salary_entry.place(x=385, y=260)

        # INSERT-btn
        self.insert_btn = Button(self.frame, font=("San Francisco", 14, "bold"), padx=10,
                                 text="INSERT", bg="#28a745", fg="white",
                                 activeforeground="#28a745", command=self.insert,
                                 cursor="hand2")
        self.insert_btn.place(x=210, y=350, width=140, height=45)

        # SEARCH-btn
        self.search_btn = Button(self.frame, font=("San Francisco", 14, "bold"), padx=10,
                                 text="SEARCH", bg="#007bff", fg="white",
                                 activeforeground="#007bff", command=self.search,
                                 cursor="hand2")
        self.search_btn.place(x=400, y=350, width=140, height=45)

        # VIEW-ALL-btn
        self.view_all_btn = Button(self.frame, font=("San Francisco", 14, "bold"), padx=10,
                                   text="VIEW ALL", bg="#e67e22", fg="white",
                                   activeforeground="#007bff", command=self.view_all,
                                   cursor="hand2")
        self.view_all_btn.place(x=590, y=350, width=140, height=45)

        # Delete-btn
        self.delete_btn = Button(self.frame, font=("San Francisco", 14, "bold"), text="DELETE", padx=10,
                                 bg="#DC3545", fg="white",
                                 cursor="hand2",
                                 activeforeground="#DC3545", command=self.delete)
        self.delete_btn.place(x=300, y=420, width=140, height=45)

        # EXIT-btn
        self.delete_btn = Button(self.frame, font=("San Francisco", 14, "bold"), text="EXIT", padx=10,
                                 bg="#ffc107", fg="white",
                                 cursor="hand2",
                                 activeforeground="#ffc107", command=self.exit)
        self.delete_btn.place(x=495, y=420, width=140, height=45)

        # Footer
        footer_label = Label(self.window, text="EMP - Employee Management System  |  Developed By Mohammad Arsalan Rather\nFor any Technical Issue Contact: 7780xxxx46",
                             bg="#c0a080", font=("Times New Roman", 12, "bold")).pack(side=BOTTOM, fill=X)

    # INSERT-btn function
    def insert(self):
        emp_id = self.emp_id.get()
        name = self.emp_name.get().title()
        dept = self.emp_dept.get().upper()
        salary = self.emp_salary.get()

        data = (emp_id, name, dept, salary)
        if not emp_id or not name or not dept or not salary:
            messagebox.showerror(
                "Empty Fields", "Fill all the required fields")
        else:
            query = "INSERT INTO employees VALUES (%d, '%s', '%s',%d)"
            self.db.execute_query(query, data)
            messagebox.showinfo("Success", "Record Inserted Successfully!")

    # search-btn function
    def search(self):
        emp_id = self.emp_id.get()
        if not emp_id:
            messagebox.showerror("Empty Fields", "Enter Employee ID to Search")
        else:
            query = "SELECT * FROM employees WHERE id = %d"
            result = self.db.search_query(query, emp_id)
            if result:
                search_record_window = Toplevel()
                search_record_window.config(bg="light yellow")
                search_record_window.title("Search Result")
                search_record_window.minsize(400, 300)
                search_record_window.maxsize(400, 300)

                head_label = Label(search_record_window, text="Search Record", font=(
                    "Arial", 20, "bold"), fg="purple", bg="light yellow", padx=20, pady=5)
                head_label.pack()
                separator = ttk.Separator(
                    search_record_window, orient="horizontal")
                separator.pack(fill="x")

                label1 = Label(search_record_window, text="Employee ID:",
                               font=("Arial", 12), bg="light yellow", fg="blue")
                label1.place(x=40, y=70)
                label2 = Label(search_record_window, text="Employee Name:",
                               font=("Arial", 12), bg="light yellow", fg="blue")
                label2.place(x=40, y=110)
                label3 = Label(search_record_window, text="Employee Department:",
                               font=("Arial", 12), bg="light yellow", fg="blue")
                label3.place(x=40, y=150)
                label4 = Label(search_record_window, text="Employee Salary:",
                               font=("Arial", 12), bg="light yellow", fg="blue")
                label4.place(x=40, y=190)

                id_label = Label(search_record_window, text=result[0],
                                 font=("Arial", 12, "bold"), bg="light yellow", fg="red")
                id_label.place(x=140, y=70)
                name_label = Label(search_record_window, text=result[1],
                                   font=("Arial", 12, "bold"), bg="light yellow", fg="red")
                name_label.place(x=170, y=110)
                dept_label = Label(search_record_window, text=result[2],
                                   font=("Arial", 12, "bold"), bg="light yellow", fg="red")
                dept_label.place(x=210, y=150)
                salary_label = Label(search_record_window, text=result[3],
                                     font=("Arial", 12, "bold"), bg="light yellow", fg="red")
                salary_label.place(x=170, y=190)

                separator_2 = ttk.Separator(
                    search_record_window, orient="horizontal")
                # Adjusted the placement of the separator
                separator_2.pack(fill="x", pady=(200, 10))

                admin_label = Label(search_record_window, text="©️Mohammad Arsalan Rather",
                                    font=("Arial", 9), bg="light yellow", fg="black")
                admin_label.place(x=105, y=260)
                print("%5d %15s %10s %10d" %
                      (result[0], result[1], result[2], result[3]))
            else:
                messagebox.showerror(
                    "Record Not Found", f"No record with Employee ID '{emp_id}' found.")

    # DELETE-btn function
    def delete(self):
        emp_id = self.emp_id.get()
        if not emp_id:
            messagebox.showerror("Empty Fields", "Enter Employee ID to Delete")
        else:
            choice = messagebox.askyesno(
                "Confirmation", "Are you sure you want to delete this record?")
            if choice:
                query = "DELETE FROM employees WHERE id = %d"
                self.db.execute_query(query, emp_id)
                messagebox.showinfo(
                    "Success", f"Record with Employee ID '{emp_id}' Deleted Successfully!")
            else:
                print("NOT Deleted")

    # VIEW-All-btn function
    def view_all(self):
        query = "SELECT * FROM employees"
        rows = self.db.execute_query(query)
        new_window = Toplevel(self.frame)
        # Create a Treeview widget with specified columns
        tree = ttk.Treeview(new_window, columns=("ID", "Name", "Department", "Salary"))
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="Department")
        tree.heading("#4", text="Salary")

        # to remove first default column
        tree["show"] = "headings"

        # Set the width of columns (adjust the values as needed)
        tree.column("#1", width=40)
        tree.column("#2", width=200)
        tree.column("#3", width=150)
        tree.column("#4", width=80)

        # Set the height of the Treeview (adjust the value as needed)
        tree["height"] = 20

        tree.pack()
        for row in rows:
            tree.insert("", "end", values=row)
            # print(row[0],row[1],row[2],row[3])
            # print("%5d %30s %23s %15d" % (row[0], row[1], row[2], row[3]))

    # EXIT-btn function
    def exit(self):
        choice = messagebox.askyesno(
            "Confirmation", "Are you sure you want to exit?")
        if choice:
            window.destroy()


if __name__ == "__main__":
    db = MyDatabase()
    window = Tk()
    main_frame = MainFrame(window, db)

    window.mainloop()
