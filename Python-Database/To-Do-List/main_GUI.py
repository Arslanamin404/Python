from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import model
import tdl_DAO

task_data = tdl_DAO.TDL_DAO()


class MainFrame:
    # constructor
    def __init__(self, window):
        self.window = window
        # self.db = db

        self.window.geometry("1000x530+250+100")
        self.window.minsize(1000, 530)
        self.window.maxsize(1000, 530)
        self.window.title("To-DO List | Developed By Mohammad Arsalan Rather")

        # heading
        self.head_label = Label(self.window,
                                text="To-DO List | Developed By Mohammad Arsalan Rather",
                                font=("Times New Roman", 20, "bold"),
                                bg="#1b1b55", fg="white", padx=20)
        self.head_label.place(x=0, y=0, relwidth=1, height=50)


        # vars
        self.task_name = StringVar()
        self.task_due_date = StringVar()
        self.task_isComplete = IntVar()

        # TAskNAME-label/Entry
        self.name_label = Label(self.window,
                                text="Task Name ",
                                font=("Arial", 14),
                                 fg="#1b1b1b")
        self.name_label.place(x=150, y=100)
        self.name_entry = Entry(self.window, textvariable=self.task_name,
                                font=("Arial", 14), fg="blue",bg="light yellow")
        self.name_entry.place(x=330, y=100, width=450)

        # TASK DESC-label/Entry
        self.desc_label = Label(self.window, text="Task Description",
                                font=("Arial", 14),
                                 fg="#1b1b1b")
        self.desc_label.place(x=150, y=150)
        self.desc_entry = Text(self.window,
                               font=("Arial", 14), fg="blue",bg="light yellow")
        self.desc_entry.place(x=330, y=150, width=450, height=120)

        # DueDate label/Entry
        self.due_date_label = Label(self.window,
                                    text="Task Due Date",
                                    font=("Arial", 14),
                                     fg="#1b1b1b")
        self.due_date_label.place(x=150, y=290)
        self.due_date_entry = Entry(self.window, textvariable=self.task_due_date,
                                    font=("Arial", 14), fg="blue",bg="light yellow")
        self.due_date_entry.place(x=330, y=290, width=450)

        # isComplete label/Entry
        self.isComplete_label = Label(self.window,
                                      text="Is Complete [0/1]",
                                      font=("Arial", 14),
                                       fg="#1b1b1b")
        self.isComplete_label.place(x=150, y=340)
        self.isComplete_entry = Entry(self.window, textvariable=self.task_isComplete,
                                      font=("Arial", 14), fg="blue",bg="light yellow")
        self.isComplete_entry.place(x=330, y=340, width=450)
        
        # =========================== Buttons ======================================
        # Add task-btn
        self.insert_btn = Button(self.window, font=("San Francisco", 14, "bold"), padx=10,
                                 text="Add Task", bg="#28a745", fg="#ffffff",
                                 activeforeground="#28a745", command=self.add_task,
                                 cursor="hand2")
        self.insert_btn.place(x=110, y=420, width=130, height=40)

        # VIEW-ALL-btn
        self.view_all_btn = Button(self.window, font=("San Francisco", 14, "bold"), padx=10,
                                   text="View Tasks", bg="#e67e22", fg="#ffffff",command=self.view_tasks,
                                   activeforeground="#007bff",
                                   cursor="hand2")
        self.view_all_btn.place(x=260, y=420, width=130, height=40)

        # markCOmplete-btn
        self.mark_complete_btn = Button(self.window, font=("San Francisco", 14, "bold"), padx=10,
                                        text="Mark as Complete", bg="#007bff", fg="#ffffff", command=self.mark_task_complete,
                                        activeforeground="#007bff",
                                        cursor="hand2")
        self.mark_complete_btn.place(x=420, y=420, width=180, height=40)

        # Delete-btn
        self.delete_btn = Button(self.window, font=("San Francisco", 14, "bold"), text="Remove Task", padx=10,
                                 bg="#DC3545", fg="#ffffff",
                                 cursor="hand2", command=self.remove_task,
                                 activeforeground="#DC3545")
        self.delete_btn.place(x=630, y=420, width=140, height=40)

        # EXIT-btn
        self.delete_btn = Button(self.window, font=("San Francisco", 14, "bold"), text="Exit", padx=10,
                                 bg="#ffc107", fg="#ffffff",
                                 cursor="hand2",
                                 activeforeground="#ffc107", command=self.exit)
        self.delete_btn.place(x=800, y=420, width=90, height=40)

    def clear_input_fields(self):
        self.task_name.set("")
        self.task_due_date.set("")
        self.desc_entry.delete("1.0", END)
        self.task_isComplete.set("")
    
    # add task function
    def add_task(self):
        try:
            if not self.task_name.get() or not self.task_due_date.get() or self.task_isComplete.get():
                messagebox.showerror("Empty Fields!","Please Fill All Required Fields!")
            else:
                task1 = model.TDL()
                task1.set_task_name(self.task_name.get())
                task1.set_task_desc(self.desc_entry.get("1.0", END)) # Get text from the Text widget
                task1.set_task_due_date(self.task_due_date.get())
                task1.set_isComplete(self.task_isComplete.get())

                task_data.add_task(task1)
                messagebox.showinfo("Success!", "Task Added Successfully!!")
                self.clear_input_fields()
        except Exception as err:
            messagebox.showerror("An Error Has Occurred!", f"{str(err)}")

    # view all tasks
    def view_tasks(self):
        task_list = task_data.view_tasks()
        new_window = Toplevel(self.window)
        
        new_window.focus_force()  # focus on window as soon as it opens
        new_window.attributes("-topmost", True)  # this attribute will keep window always on top until closed
        
        # Create a Treeview widget with specified columns
        tree = ttk.Treeview(new_window, columns=("ID", "Name", "Description", "Due Date","Is Complete"))
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="Description")
        tree.heading("#4", text="Due Date")
        tree.heading("#5", text="Is Complete")
        
        # to remove first default column
        tree["show"] = "headings"
        
        tree["height"] = 22
        
        tree.column("#1", width=40)
        tree.column("#2", width=120)
        tree.column("#3", width=400)
        tree.column("#4", width=180)
        tree.column("#5", width=80)


        tree.pack(expand=YES, fill="both")

        for task in task_list:
            task_id = task.get_task_id()
            task_name = task.get_task_name()
            task_desc = task.get_task_desc()
            task_due_date = task.get_task_due_date()
            is_complete = task.get_isComplete()
            
            tree.insert("","end",values = (task_id,task_name,task_desc,task_due_date,is_complete))
        
    
    # mark task complete
    def mark_task_complete(self):
        task_id = simpledialog.askinteger(
            "Input", "Enter Task ID To Mark as Complete: ", parent=self.window)
        result = task_data.mark_task_complete(task_id)
        if task_id is not None:
            if result is None:
                messagebox.showerror(
                    "Error 404!", f"No Task Found With Task-ID {task_id}!")
            else:
                if not result:  # result == false
                    messagebox.showwarning(
                        "Error!", "-- Task Already Marked As Complete! --")
                else:
                    messagebox.showinfo(
                        "Success", f"Task With ID {task_id} Marked As Complete Successfully!")
        else:
            messagebox.showerror(
                "Empty Field", "Enter a valid Task ID to Delete")

    # remove-btn function
    def remove_task(self):
        task_id = simpledialog.askinteger("Input", "Enter Task ID To Remove: ")
        if task_id is not None:
            result = task_data.delete_task(task_id)
            if result:
                messagebox.showinfo(
                    "Success", f"Task with Task ID '{task_id}' Removed Successfully!")
            else:
                messagebox.showerror(
                    "Error", f"Task with Task ID '{task_id}' not found.")
        else:
            messagebox.showerror(
                "Empty Field", "Enter a valid Task ID to Delete")

    # EXIT-btn function
    def exit(self):
        choice = messagebox.askyesno(
            "Confirmation", "Are you sure you want to exit?")
        if choice:
            self.window.destroy()


if __name__ == "__main__":
    window = Tk()
    main_frame = MainFrame(window)

    window.mainloop()
