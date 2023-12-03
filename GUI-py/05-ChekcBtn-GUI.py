from tkinter import *
from tkinter import messagebox


def display():
    if response.get():
        messagebox.showinfo("Agreed", "User has agreed to Terms & Conditions.")
    else:
        messagebox.showwarning(
            "Disagreed", "User didn't agreed to Terms & Conditions.")


window = Tk()
window.iconbitmap("assets/login_icon.ico")
window.title("Check Button")

photo = PhotoImage(file="assets/terms.png")

response = BooleanVar()

check_Btn = Checkbutton(window,
                        text="I agree to your terms and conditions!",
                        variable=response,
                        command=display,
                        font=("Arial", 12),
                        fg="#1B1B1B",
                        bg="#d3d3d3",
                        activebackground="#d3d3d3",
                        activeforeground="#1B1B1B",
                        padx=20,
                        pady=10,
                        image=photo,
                        compound="left"
                        )
check_Btn.pack()

window.mainloop()
