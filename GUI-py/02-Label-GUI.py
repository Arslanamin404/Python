from tkinter import *
from tkinter import font

my_window = Tk()
my_window.geometry('500x500')
my_window.title('Hello World')
my_window.iconbitmap("assets/login_icon.ico")

# fontList = list(font.families())
# for i, font in enumerate(fontList, start=1):
#     print(f"{i}. {font}")


# Create a label widget
label = Label(my_window,
              text="Welcome to My Desktop Application",
              fg="white",
              bg="#1b1b1b",
              padx=20,
              pady=10,
              font=("Tohama", 18, "italic"),
              relief=RAISED,  # border style
              bd=10  # border width
              )
label.pack()
# label.place(x=0,y=0) #position to display the label


my_window.mainloop()
