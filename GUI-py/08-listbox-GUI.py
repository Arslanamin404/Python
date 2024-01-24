from tkinter import *


def submit():
    print(f"You have ordered {listbox.get(listbox.curselection())}!")


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


items = ["Pizza", "Burger", "Pasta",
         "Biryani", "Momos", "Garlic Bread",
         "Tandoori Chicken", "Afghani Chicken"]

window = Tk()
window.title("Order your Meal!")
window.config(bg="Grey")
listbox = Listbox(window,
                  bg="#f7ffd3",
                  font=("Constantia", 18),
                  width=22)
listbox.pack()

for i, item in enumerate(items):
    listbox.insert(i, item)

# for dynamic height
listbox.config(height=listbox.size())


# entry box to add items
entryBox = Entry(window, font=("Constantia", 15))
entryBox.pack(fill=X, pady=10)

# order btn
submitBtn = Button(window, text="Order Now!", bg="orange", fg="white", padx=10,
                   font=("Arial", 12, "bold"), command=submit)
submitBtn.pack(pady=3)

# add btn
addBtn = Button(window, text="Add Item!", bg="Green", fg="white", padx=10,
                font=("Arial", 12, "bold"), command=add)
addBtn.pack(pady=3)

# add btn
delBtn = Button(window, text="Delete Item!", bg="Red", fg="white", padx=10,
                font=("Arial", 12, "bold"), command=delete)
delBtn.pack(pady=3)
window.mainloop()
