from tkinter import *
from tkinter import messagebox

food = ['Pizza', 'Burger', 'Shawarma']


def showResponse():
    if response.get() == 0:
        messagebox.showinfo("Order Info!","You ordered a Pizza! Take you order after 25 mins.🍴")
    elif response.get() == 1:
        messagebox.showinfo("Order Info!","You ordered a Burger! Take you order after 5 mins.🍴")
    elif response.get() == 2:
        messagebox.showinfo("Order Info!","You ordered a Shawarma! Take you order after 15 mins.🍴")
    else:
        print("oooops!")


window = Tk()
window.title("Order Your Food - Radio Buttons")
window.iconbitmap("assets/restaurant_icon.ico")
window.geometry("400x300")

pizza_img = PhotoImage(file="assets/pizza.png")
burger_img = PhotoImage(file="assets/burger.png")
shawarma_img = PhotoImage(file="assets/roll.png")

food_images = [pizza_img, burger_img, shawarma_img]

response = IntVar()

head = Label(window,
             text="Make your Order now!!!!",
             font=("Arial", 18),
             bg="light yellow",
             fg="purple")
head.pack()

for index in range(len(food)):
    radioBtn = Radiobutton(window,
                           text=food[index],
                           variable=response,
                           value=index,  # this assigns each radio btn a different value
                           padx=15,
                           pady=10,
                           font=("Arial", 15, "bold"),
                           image=food_images[index],
                           compound="left",
                           command=showResponse)
    # Pack the radio button into the window, left-aligned
    radioBtn.pack(anchor=W)

admin = Label(window, text="©️Mohammad Arsalan Rather")
admin.pack()

window.mainloop()
