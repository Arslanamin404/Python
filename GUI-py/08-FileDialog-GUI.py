from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(title="Open file",
                                          filetypes=(("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    with open(filepath, "r") as file:
        print(file.read())


def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML", ".html"),
                                        ("All Files", "*.*")
                                    ])
    file_text = str(text.get("1.0", END))
    file.write(file_text)
    file.close()


window = Tk()
window.title("FileDialog")
label = Label(window,
              text="Enter Text to save or open a file for reading!!!",
              font=("Arial", 18, "bold"),
              padx=20,
              pady=10)
label.pack()

text = Text(window,
            bg="#ffd7b5",
            font=("Caliber", 14),
            padx=10,
            pady=20,
            height=15,
            width=50,
            )
text.pack()

btn_save = Button(window,
                  text="Save File",
                  height=1,
                  width=10,
                  bg="RED",
                  fg="white",
                  font=("Arial", 12, "bold"),
                  command=save_file)
btn_save.pack()

btn_open = Button(window,
                  text="Read File",
                  height=1,
                  width=10,
                  bg="yellow",
                  font=("Arial", 12, "bold"),
                  command=open_file)
btn_open.pack()

window.mainloop()
