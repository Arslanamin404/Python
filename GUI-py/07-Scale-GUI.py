from tkinter import *


def submit():
    print(f"The temperature is {scale.get()}C")


window = Tk()
window.geometry("150x350")
window.maxsize(150, 350)
scale = Scale(window,
              from_=0,
              to=100,
              length=280,
              orient=VERTICAL,
              font=('Consolas',12),
              tickinterval=10,
              troughcolor="#00FF00",
              fg="#FF1C00")
scale.pack()

btn = Button(window, text="Submit", command=submit)
btn.pack()
window.mainloop()
