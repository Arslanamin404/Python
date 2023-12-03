from tkinter import *
# tk() is class which will ready our window
# this must be the first line of our gui code it is responsible to create our container
window = Tk()

window.geometry("500x500")  # size of window .geometry("WIDTHxHEIGHT").
window.maxsize(800, 800)  # max size of window (Width,height)
window.minsize(300, 300)  # min size of window (Width,height)
window.title("Test Application")  # title of window/application
window.iconbitmap("login_icon.ico")  # this will set the icon of window
window.config(background="#1b1b1b")
window.mainloop()
