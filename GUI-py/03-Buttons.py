from tkinter import *

count = 1


def click():
    global count
    print(f"Btn Click: {count}")
    count += 1


window = Tk()

window.geometry("600x600")
window.title("How to add Buttons & Event Listeners")
window.iconbitmap("assets/login_icon.ico")

photo = PhotoImage(file="assets/like.png")
btn = Button(window,
             bg="#4b4b4b",
             fg="#fff",
             text="Click Me",
             font=("Comic Sans", 20),
             command=click,
             padx=10,
             activebackground="#3b3b3b",
             activeforeground="#fff",
             #  state=DISABLED
             image=photo,
             compound="left"
             )

btn.pack()

window.mainloop()
