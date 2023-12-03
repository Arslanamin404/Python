from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


class MyFrame():
    def __init__(self, window):
        self.frame = Frame(window, width=500, height=500, bg="#1b1b1b")
        self.frame.propagate(0)
        self.frame.pack()

        self.btn = Button(self.frame,
                          text="Input Details",
                          padx=10,
                          pady=10,
                          bg="red",
                          fg="white",
                          font=("Arial", 12, "bold"),
                          command=self.btnClick)
        self.btn.place(x=200, y=200)

    def btnClick(self):
        self.name = simpledialog.askstring("Name", "What is your name?")
        self.age = simpledialog.askinteger("Age", "What is your age?")
        self.standard = simpledialog.askinteger("Class", "In which class do you study?")
        self.marks = simpledialog.askfloat("Marks Obtained", "Marks obtained in class 10")
        self.student_details = f"Name: {self.name}.\nAge: {self.age}\nClass: {self.standard}\nMarks obtained in 10th: {self.marks}"
        messagebox.showinfo("Student Details", self.student_details)


window = Tk()
window.title("Input Dialog")
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)

frame = MyFrame(window)
window.mainloop()
