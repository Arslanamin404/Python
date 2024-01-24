from tkinter import *
from tkinter import colorchooser


def get_color():
    color = colorchooser.askcolor()
    print(f"RGB {color[0]}\nHex Val {color[1]}")
    window.config(bg=color[1])


window = Tk()
window.geometry("300x300")
window.title("Color Chooser")
btn = Button(window, text="Choose Color", command=get_color)
btn.pack()
window.mainloop()
