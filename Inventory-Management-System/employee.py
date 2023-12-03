from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database_connection import IMSDataBase


class EmployeeClass:
    def __init__(self, window):
        self.ims_db = IMSDataBase()  # Create an instance of the database connection
        self.window = window
        # (width x height + defaultPositionX+defaultPositionY)
        self.window.geometry("1150x550+230+130")
        self.window.maxsize(1150, 550)
        self.window.minsize(1150, 550)
        self.window.title("Employee Details - Inventory Management System | Developed By Mohammad Arsalan Rather")
        self.window.config(bg="#F0F0F0")
        self.window.focus_force()  # focus on window as soon as it opens
        
        # this attribute will keep window always on top until closed
        self.window.attributes("-topmost", True)

        # ========= All Variable =========
        self.searchBy_var = StringVar()
        self.searchText_var = StringVar()

        self.empID_var = IntVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.name_var = StringVar()
        self.dob_var = StringVar()
        self.doj_var = StringVar()
        self.email_var = StringVar()
        self.paswd_var = StringVar()
        self.userType_var = StringVar()
        self.salary_var = IntVar()

        # ======== Search Frame ========
        search_frame = LabelFrame(self.window, text="Search Employee", bg="#F0F0F0",
                                  font=("goudy old style", 12, "bold"),
                                  bd=2, relief=RIDGE)
        search_frame.place(x=230, y=20, width=600, height=70)

        # ======== Drop-Down Search Options ==========
        search_options = ttk.Combobox(search_frame, textvariable=self.searchBy_var, values=("Select", "Email", "Name", "Emp-ID", "Contact"),
                                      state="readonly", justify=CENTER,
                                      font=("goudy old style", 15))
        search_options.place(x=10, y=10, width=180)
        search_options.current(0)  # current(0) == values[0]

        # ====== Search Entry ======
        search_entry = Entry(search_frame, bg="Light Yellow", textvariable=self.searchText_var,
                             font=("goudy old style", 15))
        search_entry.place(x=200, y=10)
        search_entry.bind("<Return>", self.search_on_return)
        

        # ====== Search Button =======
        search_btn = Button(search_frame, font=("goudy old style", 15),
                            text="Search", bg="#4caf50", fg="white",command=self.search,
                            activebackground="light grey", cursor="hand2")
        search_btn.place(x=435, y=9, width=145, height=30)

        # ======== Title ========
        title = Label(self.window, text="Employee Details",
                      bg="#0f4d7d", fg="white",
                      font=("goudy old style", 15))
        title.place(x=50, y=100, width=1050)

        # ============ Content Labels ============
        # ==================== Row 01 ====================
        empID_label = Label(self.window, text="EMP ID ", bg="#F0F0F0",
                            font=("Times New Roman", 15)).place(x=80, y=150)

        gender_label = Label(self.window, text="Gender ", bg="#F0F0F0",
                             font=("Times New Roman", 15)).place(x=470, y=150)
        contact_label = Label(self.window, text="Contact ", bg="#F0F0F0",
                              font=("Times New Roman", 15)).place(x=800, y=150)

        # =========== Content Entry ===========
        empID_entry = Entry(self.window, bg="light yellow", textvariable=self.empID_var,
                            font=("Arial", 12)).place(x=180, y=150, width=230)

        # ======== Drop-Down Gender Options ==========
        gender_options = ttk.Combobox(self.window, textvariable=self.gender_var, values=("Select", "Male", "Female"),
                                      state="readonly", justify=CENTER,
                                      font=("Times New Roman", 14))
        gender_options.place(x=560, y=150, width=180)
        gender_options.current(0)  # current(0) == values[0]

        contact_entry = Entry(self.window, bg="light yellow", textvariable=self.contact_var,
                              font=("Arial", 12)).place(x=900, y=150, width=180)

        # ==================== Row 02 ====================
        name_label = Label(self.window, text="Name ", bg="#F0F0F0",
                           font=("Times New Roman", 15)).place(x=80, y=190)

        dob_label = Label(self.window, text="D.O.B ", bg="#F0F0F0",
                          font=("Times New Roman", 15)).place(x=470, y=190)
        dob = j_label = Label(self.window, text="D.O.J ", bg="#F0F0F0",
                              font=("Times New Roman", 15)).place(x=800, y=190)

        # =========== Row 02 Entry ===========
        name_entry = Entry(self.window, bg="light yellow", textvariable=self.name_var,
                           font=("Arial", 12)).place(x=180, y=190, width=230)
        dob_entry = Entry(self.window, bg="light yellow", textvariable=self.dob_var,
                          font=("Arial", 12)).place(x=560, y=190, width=180)

        doj_entry = Entry(self.window, bg="light yellow", textvariable=self.doj_var,
                          font=("Arial", 12)).place(x=900, y=190, width=180)

        # ==================== Row 03 ====================
        email_label = Label(self.window, text="Email", bg="#F0F0F0",
                            font=("Times New Roman", 15)).place(x=80, y=230)
        password_label = Label(self.window, text="Password", bg="#F0F0F0",
                               font=("Times New Roman", 15)).place(x=470, y=230)
        uType_label = Label(self.window, text="User-Type", bg="#F0F0F0",
                            font=("Times New Roman", 15)).place(x=800, y=230)

        # =========== Row 03 Entry ===========
        email_entry = Entry(self.window, bg="light yellow", textvariable=self.email_var,
                            font=("Arial", 12)).place(x=180, y=230, width=230)
        password_entry = Entry(self.window, bg="light yellow", textvariable=self.paswd_var,
                               font=("Arial", 12), show="*").place(x=560, y=230, width=180)

        # ======== Drop-Down User Type Options ==========
        uType_options = ttk.Combobox(self.window, textvariable=self.userType_var, values=("Select", "Admin", "Employee"),
                                     state="readonly", justify=CENTER,
                                     font=("Arial", 14))
        uType_options.place(x=900, y=230, width=180)
        uType_options.current(0)  # current(0) == values[0]

        # ==================== Row 4 ====================
        address_label = Label(self.window, text="Address", bg="#F0F0F0",
                              font=("Times New Roman", 15)).place(x=80, y=270)
        salary_label = Label(self.window, text="Salary", bg="#F0F0F0",
                             font=("Times New Roman", 15)).place(x=560, y=270)

        # =========== Row 04 Entry ===========
        self.address_entry = Text(self.window, bg="light yellow",
                                  font=("Arial", 12))
        self.address_entry.place(x=180, y=270, width=300, height=60)
        salary_entry = Entry(self.window, bg="light yellow", textvariable=self.salary_var,
                             font=("Arial", 12)).place(x=630, y=270, width=170)

        # ========= CRUD Buttons =========
        save_btn = Button(self.window, font=("goudy old style", 15), command=self.save,
                          text="Save", bg="#2196f3", fg="white", activebackground="light grey",
                          cursor="hand2").place(x=560, y=305, width=110, height=28)

        update_btn = Button(self.window, font=("goudy old style", 15),command=self.update,
                            text="Update", bg="#4caf50", fg="white", activebackground="light grey",
                            cursor="hand2").place(x=680, y=305, width=110, height=28)

        delete_btn = Button(self.window, font=("goudy old style", 15), command=self.delete,
                            text="Delete", bg="#f44336", fg="white", activebackground="light grey",
                            cursor="hand2").place(x=800, y=305, width=110, height=28)

        clear_btn = Button(self.window, font=("goudy old style", 15), command=self.clear,
                           text="Clear", bg="#607d8b", fg="white", activebackground="light grey",
                           cursor="hand2").place(x=920, y=305, width=110, height=28)

        # ========== Employee Details ==========
        emp_frame = Frame(self.window, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=170)

        # ========= scroll bar =========
        scroll_y = Scrollbar(emp_frame, orient=VERTICAL)
        scroll_x = Scrollbar(emp_frame, orient=HORIZONTAL)

        # ========== Tree View ==========
        self.employee_table = ttk.Treeview(emp_frame, columns=("emp_id", "name", "email", "gender", "contact", "dob",
                                           "doj", "password", "utype", "address", "salary"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        # Functional Scroll Bar
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        # defining columns
        self.employee_table.heading("emp_id", text="EMP-ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("contact", text="Contact")
        self.employee_table.heading("dob", text="D.O.B")
        self.employee_table.heading("doj", text="D.O.J")
        self.employee_table.heading("password", text="Password")
        self.employee_table.heading("utype", text="User-Type")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("salary", text="Salary")

        # to remove first default column
        self.employee_table["show"] = "headings"

        # set width of each column
        self.employee_table.column("emp_id", width=50)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("contact", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("password", width=100)
        self.employee_table.column("utype", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("salary", width=100)
        self.employee_table.pack(fill=BOTH, expand=True)
        
        # button release --> will fire on click
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        
        self.show() #this will display all records as soon as program runs
        

    # ===================================================================================================================================

    def save(self):
        try:
            if self.empID_var.get() == "" or self.email_var.get() == "" or self.salary_var.get() == "" or self.doj_var.get() == "" or self.contact_var.get() == "" or self.userType_var.get() == "Select":
                messagebox.showerror("Error", "Please Fill All Required Fields!", parent=self.window)
            else:
                query = "SELECT * FROM employee where emp_id = %s"
                # create tuple of data to pass else it will not work
                data = (self.empID_var.get(),)
                row = self.ims_db.execute_query(query, data)
                if row:
                    messagebox.showerror("Duplicate Entry", f"Employee with ID {self.empID_var.get()} already exists!",parent=self.window)
                else:
                    query = "INSERT INTO employee (emp_id, name, email, gender, contact, dob, doj, password, utype, address, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                    # create tuple of data to be inserted in db else it wont work
                    data = (self.empID_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.doj_var.get(), self.paswd_var.get(), self.userType_var.get(), self.address_entry.get("1.0", END), self.salary_var.get())

                    self.ims_db.execute_query(query, data)
                    messagebox.showinfo("Success!", "Record Inserted Successfully!",parent=self.window)
                    self.show()
                    self.clear()

        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}",parent=self.window)

    def show(self):
        try:
            query = "SELECT * FROM employee"
            rows = self.ims_db.execute_query(query)
            # to delete previous data from tree view and then updates
            self.employee_table.delete(*self.employee_table.get_children())
            if not rows:
                self.employee_table.insert("",END,values="No Record present in Database. Please add some records!")
            for row in rows:
                self.employee_table.insert("",END,values = row)
                
        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}",parent=self.window)

    # this function is bind to button click
    def get_data(self,event):
        focus = self.employee_table.focus()
        content = (self.employee_table.item(focus))
        row = content['values']

        self.empID_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.doj_var.set(row[6])
        self.paswd_var.set(row[7])
        self.userType_var.set(row[8])
        self.address_entry.delete("1.0",END)
        self.address_entry.insert(END,row[9])
        self.salary_var.set(row[10])

    def update(self):
        try:
            if self.empID_var.get() == "":
                messagebox.showerror("Error", "Please enter Employee ID to Update!", parent=self.window)
            else:
                query = "SELECT * FROM employee where emp_id = %s"
                data = (self.empID_var.get(),)
                row = self.ims_db.execute_query(query, data)
                if not row:
                    messagebox.showerror("Invalid Input", f"Employee with ID {self.empID_var.get()} does not exist!",parent=self.window)
                else:
                    query = "UPDATE employee SET name = %s, email = %s, gender = %s, contact = %s, dob = %s, doj = %s, password = %s, utype = %s, address = %s, salary = %s WHERE emp_id = %s"
                    data = (self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.doj_var.get(), self.paswd_var.get(), self.userType_var.get(), self.address_entry.get("1.0", END), self.salary_var.get(), self.empID_var.get())

                    self.ims_db.execute_query(query, data)
                    messagebox.showinfo("Success!", "Record Updated Successfully!",parent=self.window)
                    self.show()

        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}",parent=self.window)

    def delete(self):
        try:
            if self.empID_var.get() == "":
                messagebox.showerror("Error", "Please Enter the Employee ID to Delete!", parent=self.window)
            else:
                data = (self.empID_var.get(),)
                query = "SELECT * FROM employee where emp_id = %s"
                row = self.ims_db.execute_query(query, data)
                if not row:
                    messagebox.showerror("Invalid ID", f"Employee with ID {self.empID_var.get()} does not exists!",parent=self.window)
                else:
                    query = "DELETE FROM employee WHERE emp_id = %s"
                    data = (self.empID_var.get(),)
                    choice = messagebox.askyesno("Confirmation","Are you sure you want to delete this record?",parent=self.window)
                    if choice:
                        self.ims_db.execute_query(query, data)
                        messagebox.showinfo("Success", "Record Deleted Successfully!",parent=self.window)
                        self.show()
        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}",parent=self.window)

    def clear(self):
        self.searchText_var.set("")
        self.searchBy_var.set("Select")
        self.empID_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("Select")
        self.contact_var.set("")
        self.dob_var.set("")
        self.doj_var.set("")
        self.paswd_var.set("")
        self.userType_var.set("Select")
        self.address_entry.delete("1.0",END)
        self.salary_var.set("")
        
        self.show()
        
        
    def search(self):
        try:
            if self.searchBy_var.get() == "Select":
                messagebox.showerror("Error", "Please select Search BY option", parent=self.window)
            else:
                search_value = self.searchText_var.get()  # Get the search value

                if self.searchBy_var.get() == "Email":
                    query = "SELECT * FROM employee WHERE email LIKE %s"
                elif self.searchBy_var.get() == "Name":
                    query = "SELECT * FROM employee WHERE name LIKE %s"
                elif self.searchBy_var.get() == "Emp-ID":
                    query = "SELECT * FROM employee WHERE emp_id LIKE %s"
                elif self.searchBy_var.get() == "Contact":
                    query = "SELECT * FROM employee WHERE contact LIKE %s"
                else:
                    return

            # If search_value is "John," then ('%' + search_value + '%',) becomes '%John%'.
            # In your SQL query, this would search for all records where the specified column contains 'John' as a substring,
            # whether it's at the beginning, middle, or end of the text

                data = ('%' + search_value + '%',) 
                result = self.ims_db.execute_query(query, data)

                # Clear the tree view
                self.employee_table.delete(*self.employee_table.get_children())

                if not result:
                    messagebox.showerror("No Records Found!", "No Employee exists with this search criteria.", parent=self.window)
                else:
                    for row in result:
                        self.employee_table.insert("", END, values=row)

        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}", parent=self.window)

    # this function is bind to enter key
    def search_on_return(self,event):
        self.search() # Call the search function when <Return> is pressed

                
if __name__ == "__main__":
    window = Tk()
    IMS = EmployeeClass(window)
    window.mainloop()
