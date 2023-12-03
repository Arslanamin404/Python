from tkinter import *
from tkinter import messagebox


def submit():
    userInput = text.get("1.0", END)
    try:
        with open("notes_DB.txt", "a") as file:
            file.write(f"{userInput}\n")
    except Exception as err:
        print(f"😔Error! Something unexpected occurred : {err}")
        messagebox.showinfo(f"😔Error!", "Something unexpected occurred : {err}")
    else:
        print("Notes saved successfully!✅")
        messagebox.showinfo("Success!", "Note Saved Successfully to notes_DD.txt file.✅")


window = Tk()
window.title("NoteCraft: Crafting Your Thoughts - Mohammad Arsalan Rather")
window.iconbitmap("assets/notes_icon.ico")

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20),
            height=10,
            width=30,
            padx=20,
            pady=20,
            fg="purple"
            )

text.pack()
btn = Button(window,
             padx=20,
             fg="white",
             bg="#1b1b1b",
             activeforeground="white",
             activebackground="#6b6b6b",
             font=("Arial", 15),
             text="Submit",
             command=submit)
btn.pack()
admin = Label(window, text="©️Mohammad Arsalan Rather")
admin.pack()

window.mainloop()
