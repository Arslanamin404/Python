from tkinter import *
# entry widget = textbox that accepts a single line of user input


def submit():
    username = entry.get()
    print(f"Hello {username}! Welcome to my program")
    entry.config(state=DISABLED)  # textbox will be disabled after submit


def delete():
    entry.delete(0, END)


window = Tk()
window.title("Entry Box - TextBox")
window.iconbitmap("assets/login_icon.ico")
entry = Entry(window,
              font=("Arial,18"),
              fg="#00FF00",
              bg="black",
              show="*") #used to hide passwords

# entry.insert(0, "username")  # default value
entry.pack(side=LEFT)

submitBtn = Button(window, text="Submit", command=submit)
submitBtn.pack(side=LEFT)

deleteBtn = Button(window, text="Delete", command=delete)
deleteBtn.pack(side=RIGHT)


window.mainloop()
