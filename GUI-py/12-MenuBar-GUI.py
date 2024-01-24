from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def new_file():
    content = text.get("1.0", END).strip()
    if content:
        res = messagebox.askyesno(
            "Warning!", "Are you sure you want to continue?", icon="warning")
        if res:
            text.delete("1.0", END)


def open_file():
    filepath = filedialog.askopenfilename(title="Open file",
                                          filetypes=(("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    with open(filepath, "r") as file:
        File_content = file.read()
        if text.get("1.0", END).strip():
            text.delete("1,0", END)  # clear existing data on screen
        text.insert(END, File_content)
    window.title(f"Notepad - {filepath}")


def save_file():
    try:
        file = filedialog.asksaveasfile(defaultextension='.txt',
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML", ".html"),
                                            ("All Files", "*.*")
                                        ])
        file_text = str(text.get("1.0", END))
        file.write(file_text)
        messagebox.showinfo("Success!", "File saved successfully!")
    except Exception as err:
        messagebox.showwarning(
            "Something unexpected occurred!", f"Error: {err}")
    finally:
        file.close()
        print("File Closed")


def cut():
    selected_txt = text.get("sel.first", "sel.last")
    window.clipboard_clear()
    window.clipboard_append(selected_txt)
    text.delete("sel.first", "sel.last")


def copy():
    selected_txt = text.get("sel.first", "sel.last")
    window.clipboard_clear()
    window.clipboard_append(selected_txt)


def paste():
    clipboard_data = window.clipboard_get()
    text.insert(END, clipboard_data)


window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
window.title("Mini Notepad")

fileMenu = Menu(menubar, tearoff=0, font=("Arial", 10))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


editMenu = Menu(menubar, tearoff=0, font=("Arial", 10))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_separator()
editMenu.add_command(label="Paste", command=paste)

text = Text(window,
            font=("Arial", 12),
            padx=10, pady=20)
text.pack()
window.mainloop()
