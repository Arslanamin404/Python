from tkinter import *
from tkinter import messagebox


class UserDetails():
    def __init__(self, window):
        self.frame = Frame(window,
                           width=500,
                           height=500,
                           bg="#1b1b1b")
        self.frame.propagate(0)
        self.frame.pack()

        self.heading = Label(self.frame,
                             text="Dummy Registration Page",
                             font=("Comic Sans MS", 14, "bold"),
                             padx=30, pady=2,
                             bg="#AFF500")

        self.heading.place(x=60, y=10)

        self.name_label = Label(self.frame,
                                text="Username ",
                                font=("Arial", 10))
        self.name_label.place(x=70, y=100)
        self.name = Entry(self.frame, font=("Arial", 12))
        self.name.place(x=140, y=100)

        self.password_label = Label(self.frame,
                                    text="Password ",
                                    font=("Arial", 10))
        self.password_label.place(x=70, y=140)
        self.password = Entry(self.frame, font=("Arial", 12), show="*")
        self.password.place(x=140, y=140)
        # this will display the name value when user hits Enter (Return Btn)
        self.password.bind("<Return>", self.check)

        self.btn = Button(self.frame,
                          font=("Arial", 10),
                          text="Register",
                          padx=10,
                          command=self.register)
        self.btn.place(x=170, y=180)

        self.detail = Label(self.frame,
                            text="User Details: ",
                            font=("Arial", 10))

        self.detail.place(x=120, y=250)

    def register(self):
        username = self.name.get()
        password = self.password.get()
        if not username.strip() or not password.strip():
            messagebox.showerror("Error - Empty Fields",
                                 "Username and Password are required.")
        else:
            messagebox.showinfo("Success!", "Registered Successfully!")
            n = self.name.get()
            p = self.password.get()
            self.detail["text"] = f"Username: {n}\nPassword: {p}"

    def check(self, event):
        self.register()


if __name__ == "__main__":
    window = Tk()
    window.geometry("400x400")
    window.minsize(400, 400)
    window.maxsize(400, 400)
    window.title("Register - Frame - using Oop")
    window.iconbitmap("assets/login_icon_02.ico")

    user_frame = UserDetails(window)

    window.mainloop()
