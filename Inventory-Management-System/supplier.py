from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database_connection import IMSDataBase


class SupplierClass:
    def __init__(self, window):
        self.ims_db = IMSDataBase()  # Create an instance of the database connection
        self.window = window
        # (width x height + defaultPositionX+defaultPositionY)
        self.window.geometry("1150x550+230+130")
        self.window.maxsize(1150, 550)
        self.window.minsize(1150, 550)
        self.window.title("Supplier Details - Inventory Management System | Developed By Mohammad Arsalan Rather")
        self.window.config(bg="#F0F0F0")
        self.window.focus_force()  # focus on window as soon as it opens

        # this attribute will keep window always on top until closed
        self.window.attributes("-topmost", True)

        # ========= All Variable =========
        self.searchText_var = StringVar()

        self.supplier_invoice_var = IntVar()
        self.contact_var = StringVar()
        self.name_var = StringVar()

        # ========  Search  ==========
        search_label = Label(self.window,text="Invoice No. ",
                                      font=("Times New Roman", 15))
        search_label.place(x=700, y=80)
       
        # ====== Search Entry ======
        search_entry = Entry(self.window, bg="Light Yellow", textvariable=self.searchText_var,
                             font=("goudy old style", 15))
        search_entry.place(x=810, y=80,width=180)
        search_entry.bind("<Return>", self.search_on_return)

        # ====== Search Button =======
        search_btn = Button(self.window, font=("goudy old style", 15),
                            text="Search", bg="#4caf50", fg="white", command=self.search,
                            activebackground="light grey", cursor="hand2")
        search_btn.place(x=1000, y=80, width=100, height=30)

        # ======== Title ========
        title = Label(self.window, text="Supplier Details",
                      bg="#0f4d7d", fg="white",
                      font=("goudy old style", 20,"bold"))
        title.place(x=50, y=10, width=1050,height=40)

        # ============ Content Labels ============
        # ==================== Row 01 ====================
        supplier_invoice_label = Label(self.window, text="Invoice No.", bg="#F0F0F0",
                                       font=("Times New Roman", 15)).place(x=80, y=80)
        supplier_invoice_entry = Entry(self.window, bg="light yellow", textvariable=self.supplier_invoice_var,
                                       font=("Arial", 12)).place(x=200, y=80, width=230)

        # ==================== Row 02 ====================
        name_label = Label(self.window, text="Name ", bg="#F0F0F0",
                           font=("Times New Roman", 15)).place(x=80, y=120)
        name_entry = Entry(self.window, bg="light yellow", textvariable=self.name_var,
                           font=("Arial", 12)).place(x=200, y=120, width=230)

        # ==================== Row 03 ====================
        contact_label = Label(self.window, text="Contact", bg="#F0F0F0",
                              font=("Times New Roman", 15)).place(x=80, y=160)
        contact_entry = Entry(self.window, bg="light yellow", textvariable=self.contact_var,
                              font=("Arial", 12)).place(x=200, y=160, width=230)

        # ==================== Row 4 ====================
        description_label = Label(self.window, text="Description", bg="#F0F0F0",
                                  font=("Times New Roman", 15)).place(x=80, y=200)
        self.description_entry = Text(self.window, bg="light yellow",
                                      font=("Arial", 12))
        self.description_entry.place(x=200, y=200, width=470, height=130)

        # ========= CRUD Buttons =========
        save_btn = Button(self.window, font=("goudy old style", 15), command=self.save,
                          text="Save", bg="#2196f3", fg="white", activebackground="light grey",
                          cursor="hand2").place(x=200, y=370, width=110, height=35)

        update_btn = Button(self.window, font=("goudy old style", 15), command=self.update,
                            text="Update", bg="#4caf50", fg="white", activebackground="light grey",
                            cursor="hand2").place(x=320, y=370, width=110, height=35)

        delete_btn = Button(self.window, font=("goudy old style", 15), command=self.delete,
                            text="Delete", bg="#f44336", fg="white", activebackground="light grey",
                            cursor="hand2").place(x=440, y=370, width=110, height=35)

        clear_btn = Button(self.window, font=("goudy old style", 15), command=self.clear,
                           text="Clear", bg="#607d8b", fg="white", activebackground="light grey",
                           cursor="hand2").place(x=560, y=370, width=110, height=35)

        # ========== Employee Details ==========
        emp_frame = Frame(self.window, bd=3, relief=RIDGE)
        emp_frame.place(x=710, y=120, width=430, height=350)

        # ========= scroll bar =========
        scroll_y = Scrollbar(emp_frame, orient=VERTICAL)
        scroll_x = Scrollbar(emp_frame, orient=HORIZONTAL)

        # ========== Tree View ==========
        self.supplier_table = ttk.Treeview(emp_frame, columns=(
            "invoice", "name", "contact", "description"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        # Functional Scroll Bar
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.supplier_table.xview)
        scroll_y.config(command=self.supplier_table.yview)

        # defining columns
        self.supplier_table.heading("invoice", text="Invoice")
        self.supplier_table.heading("name", text="Name")
        self.supplier_table.heading("contact", text="Contact")
        self.supplier_table.heading("description", text="Description")

        # to remove first default column
        self.supplier_table["show"] = "headings"

        # set width of each column
        self.supplier_table.column("invoice", width=40)
        self.supplier_table.column("name", width=100)
        self.supplier_table.column("contact", width=30)
        self.supplier_table.column("description", width=200)
        
        # Add this line to pack the Treeview
        self.supplier_table.pack(fill=BOTH, expand=1)
        # button release --> will fire on click
        self.supplier_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()  # this will display all records as soon as program runs

    # ===================================================================================================================================

    def save(self):
        try:
            if self.supplier_invoice_var.get() == "" or self.name_var.get() == "" or self.contact_var.get() == "":
                messagebox.showerror("Error", "Please Fill All Required Fields!", parent=self.window)
            else:
                query = "SELECT * FROM supplier where invoice = %s"
                # create tuple of data to pass else it will not work
                data = (self.supplier_invoice_var.get(),)
                row = self.ims_db.execute_query(query, data)
                if row:
                    messagebox.showerror("Duplicate Entry", f"Invoice no. {self.supplier_invoice_var.get()} already assigned, try different!", parent=self.window)
                else:
                    query = "INSERT INTO supplier (invoice, name, contact, description) VALUES (%s, %s, %s, %s)"

                    # create tuple of data to be inserted in db else it wont work
                    data = (self.supplier_invoice_var.get(),
                            self.name_var.get(),
                            self.contact_var.get(),
                            self.description_entry.get("1.0", END))

                    self.ims_db.execute_query(query, data)
                    messagebox.showinfo(
                        "Success!", "Record Inserted Successfully!", parent=self.window)
                    self.show()
                    self.clear()

        except Exception as err:
            messagebox.showerror(
                "Error", f"An Error Has Occurred: {str(err)}", parent=self.window)

    def show(self):
        try:
            query = "SELECT * FROM supplier"
            rows = self.ims_db.execute_query(query)
            
            # Clear the Treeview before inserting new data
            self.supplier_table.delete(*self.supplier_table.get_children())
            
            if not rows:
                # Display a message in the Treeview if there are no records
                self.supplier_table.insert("", END, values=("No records found in the database.", "", "", ""))
            else:
                for row in rows:
                    self.supplier_table.insert("", END, values=row)

        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}", parent=self.window)

    # this function is bind to button click
    def get_data(self, event):
        focus = self.supplier_table.focus()
        content = (self.supplier_table.item(focus))
        row = content['values']

        self.supplier_invoice_var.set(row[0])
        self.name_var.set(row[1])
        self.contact_var.set(row[2])
        self.description_entry.delete("1.0", END)
        self.description_entry.insert(END, row[3])

    def update(self):
        try:
            if self.supplier_invoice_var.get() == "":
                messagebox.showerror(
                    "Error", "Please enter Invoice No. to Update!", parent=self.window)
            else:
                query = "SELECT * FROM supplier where invoice = %s"
                data = (self.supplier_invoice_var.get(),)
                row = self.ims_db.execute_query(query, data)
                if not row:
                    messagebox.showerror(
                        "Invalid Input", f"Invoice No. {self.supplier_invoice_var.get()} does not exist!", parent=self.window)
                else:
                    query = "UPDATE supplier SET name = %s, contact = %s, description = %s WHERE invoice = %s"
                    data = (self.name_var.get(),
                            self.contact_var.get(),
                            self.description_entry.get("1.0", END),
                            self.supplier_invoice_var.get())

                    self.ims_db.execute_query(query, data)
                    messagebox.showinfo("Success!", "Record Updated Successfully!", parent=self.window)
                    self.show()

        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}", parent=self.window)

    def delete(self):
        try:
            if self.supplier_invoice_var.get() == "":
                messagebox.showerror("Error", "Please Enter the Invoice No. to Delete!", parent=self.window)
            else:
                data = (self.supplier_invoice_var.get(),)
                query = "SELECT * FROM supplier WHERE invoice = %s"
                row = self.ims_db.execute_query(query, data)
                if not row:
                    messagebox.showerror("Invalid Invoice No.", f"Invoice No. {self.supplier_invoice_var.get()} does not exist!", parent=self.window)
                else:
                    choice = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?", parent=self.window)
                    if choice:
                        query = "DELETE FROM supplier WHERE invoice = %s"
                        self.ims_db.execute_query(query, data)
                        messagebox.showinfo("Success", "Record Deleted Successfully!", parent=self.window)
                        self.show()
        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}", parent=self.window)

    def clear(self):
        self.searchText_var.set("")
        self.supplier_invoice_var.set("")
        self.name_var.set("")
        self.contact_var.set("")
        self.description_entry.delete("1.0", END)

        self.show()


    def search(self):
        try:
            search_value = self.searchText_var.get().strip()
            if not search_value:
                messagebox.showerror("Error", "Invoice Number is required!", parent=self.window)
            else:
                query = "SELECT * FROM supplier WHERE invoice LIKE %s"
                data = ('%' + search_value + '%',)
                result = self.ims_db.execute_query(query, data)
                self.supplier_table.delete(*self.supplier_table.get_children())
                if not result:
                    messagebox.showerror("No Records Found!", "No Supplier exists with this Invoice No.", parent=self.window)
                else:
                    for row in result:
                        self.supplier_table.insert("", END, values=row)

        except Exception as err:
            messagebox.showerror("Error", f"An Error Has Occurred: {str(err)}", parent=self.window)

    # this function is bind to enter key
    def search_on_return(self, event):
        self.search()  # Call the search function when <Return> is pressed



if __name__ == "__main__":
    window = Tk()
    IMS = SupplierClass(window)
    window.mainloop()
