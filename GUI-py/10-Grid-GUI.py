from tkinter import *
from tkinter import messagebox


class MyGrid():
    def __init__(self, window):
        self.label = Label(text="Enter Your Height in cm: ",
                           font=("Comic Sans MS", 14, "bold"),
                           bg="#AFF500")
        self.IntValue = IntVar()
        self.number = Entry(textvariable=self.IntValue,
                            font=("Arial", 14, "bold"),
                            width=10)
        self.number.bind("<Return>", self.returnFunc)

        self.btn = Button(text="Check",
                          font=("Arial", 12, "bold"),
                          bg="blue", fg="white",
                          command=self.check)

        self.label.grid(row=0, column=0)
        self.number.grid(row=0, column=1)
        self.btn.place(x=150, y=50)

    def check(self):
        height = int(self.number.get())
        if height < 20:
            messagebox.showerror("Error! - Empty Field",
                                 "Please enter a valid hight")
        else:
            msg = f"Your Height is {height} cm's."
            messagebox.showinfo("Height", msg)

    def returnFunc(self, event):
        self.check()


if __name__ == "__main__":
    window = Tk()
    window.geometry("400x400")
    window.minsize(400, 400)
    window.maxsize(400, 400)
    window.title("Grid - using Oop")
    my_grid_label = MyGrid(window)
    window.mainloop()
