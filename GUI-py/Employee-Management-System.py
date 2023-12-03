from tkinter import *
from tkinter import messagebox

class MainFrame:
    def __init__(self, window):
        self.frame = Frame(window, width=600, height=400, bg="#1b1b1b")
        self.frame.propagate(0)
        self.frame.pack()
        
        self.head_label = Label(self.frame, text="Employee Management System", font=("Segoe Script", 18, "bold"),bg="#333333",fg="#39FF14",padx=20)
        self.head_label.pack()
        
        self.emp_id = IntVar()
        self.emp_name = StringVar()
        self.emp_dept = StringVar()
        self.emp_salary = IntVar()

        self.id_label = Label(self.frame, text="Employee ID:", font=("Arial", 12, "bold"),bg="#1b1b1b",fg="white")
        self.id_label.place(x=10, y=70)
        
        self.id_entry = Entry(self.frame,font=("Arial", 12, "bold"),textvariable=self.emp_id,width=10)
        self.id_entry.place(x=120,y=73)

        self.name_label = Label(self.frame, text="Employee Name:", font=("Arial", 12, "bold"),bg="#1b1b1b",fg="white")
        self.name_label.place(x=10, y=120)
        
        self.name_entry = Entry(self.frame,font=("Arial", 12, "bold"),textvariable=self.emp_name,width=40)
        self.name_entry.place(x=150,y=123)
        
        self.dept_label = Label(self.frame, text="Employee Department:", font=("Arial", 12, "bold"),bg="#1b1b1b",fg="white")
        self.dept_label.place(x=10, y=170)
        
        self.dept_entry = Entry(self.frame,font=("Arial", 12, "bold"),textvariable=self.emp_dept,width=30)
        self.dept_entry.place(x=190,y=173)
        
        self.salary_label = Label(self.frame, text="Employee Salary:", font=("Arial", 12, "bold"),bg="#1b1b1b",fg="white")
        self.salary_label.place(x=10, y=220)
        
        self.salary_entry = Entry(self.frame,font=("Arial", 12, "bold"),textvariable=self.emp_salary,width=20)
        self.salary_entry.place(x=160,y=223)
        
        self.insert_btn = Button(self.frame,text="Insert Record",font=("Arial", 12, "bold"),bg="#39FF14",activebackground="black",activeforeground="White",padx=10,command=self.insert_record)
        self.insert_btn.place(x=50,y=280)
        
        self.delete_btn = Button(self.frame,text="Delete Record",font=("Arial", 12, "bold"),bg="Red",fg="white",activebackground="black",activeforeground="White",padx=10,command=self.delete_record)
        self.delete_btn.place(x=220,y=280)
        
        self.search_btn = Button(self.frame,text="Search Record",font=("Arial", 12, "bold"),bg="Blue",fg="white",activebackground="black",activeforeground="White",padx=10,command=self.search_record)
        self.search_btn.place(x=400,y=280)
        
        self.admin_label = Label(self.frame, text="©️Mohammad Arsalan Rather", font=("Arial", 9),bg="#1b1b1b",fg="white") 
        self.admin_label.place(x=200,y=360)
        
    def insert_record(self):
        emp_id = self.emp_id.get() 
        name = self.emp_name.get().title()
        dept = self.emp_dept.get().upper()
        salary = self.emp_salary.get()
        
        if not emp_id or not name or not dept or not salary:
            messagebox.showerror("Empty Fields","Fill all the required fields")
        else:
            print(f"Record Inserted")
            msg =f"Employee ID: {emp_id}\nEmployee Name: {name}\nDepartment: {dept}\nSalary: {salary}" 
            messagebox.showinfo("Record Inserted",msg)
        # to be continue 
        
    def delete_record(self):
        emp_id = self.emp_id.get() 
        name = self.emp_name.get().title()
        dept = self.emp_dept.get().upper()
        salary = self.emp_salary.get()
        
        if not emp_id or not name or not dept or not salary:
            messagebox.showerror("Empty Fields","Fill all the required fields")
        else:
            print("Record Deleted")
            msg =f"Employee ID: {emp_id}\nEmployee Name: {name}\nDepartment: {dept}\nSalary: {salary}" 
            messagebox.showwarning("Record Deleted!",msg)
        # to be continue
        
    def search_record(self):
        emp_id = self.emp_id.get() 
        name = self.emp_name.get().title()
        dept = self.emp_dept.get().upper()
        salary = self.emp_salary.get()
        
        if not emp_id or not name or not dept or not salary:
            messagebox.showerror("Empty Fields","Fill all the required fields")
        else:
            print("Record Searched")
        # to be continue
        
        
if __name__ == "__main__":
    window = Tk()
    window.title("Employee Management System")
    window.geometry("600x400")
    window.minsize(600,400)
    window.maxsize(600,400)
    main_frame = MainFrame(window)
    window.mainloop()
        