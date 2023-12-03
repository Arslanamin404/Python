from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from employee import EmployeeClass
from supplier import SupplierClass


class InventoryManagementSystem:
    def __init__(self, window):
        self.window = window
        # (width x height + defaultPositionX+defaultPositionY)
        self.window.geometry("1400x700+40+40")
        self.window.title(
            "Inventory Management System | Developed By Mohammad Arsalan Rather")
        self.window.config(bg="white")

        # self. udar use karna hai joh hum aage baki methods me use honge

        # ======== TITLE =========
        self.title_icon = PhotoImage(file="assets/cart.png")
        title_label = Label(self.window, text="Inventory Management System", image=self.title_icon, compound=LEFT, bg="#010c48",
                            fg="white", anchor="w", padx=20, font=("Times New Roman", 40, "bold")).place(x=0, y=0, relwidth=1, height=70)
        # relwidth--> relative width = 1 ===> takes width of parent width i.e window

        # ======== Logout Button ============
        Logout_btn = Button(self.window, text="Logout", fg="white", bg="#FE0000", activebackground="#010c48", activeforeground="white",
                            cursor="hand2", font=("Times New Roman", 16, "bold")).place(x=1250, y=15, width=140, height=40)

        # ======== Clock Label ==================
        self.clock_label = Label(self.window, text="Welcome to Inventory Management System \t\t Date: DD-MM-YYYY \t\t Time: HH-MM-SS",
                                 bg="#4d636d", fg="white", font=("Times New Roman", 14))
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # ======= Resize Side Menu icon ===============
        self.left_menu_icon = Image.open("assets/warehouse.png")
        self.left_menu_icon = self.left_menu_icon.resize((200, 250))
        self.left_menu_icon = ImageTk.PhotoImage(self.left_menu_icon)

        # ======= Side Menu ===============
        side_menu = Frame(self.window, bd=2, relief=RIDGE, bg="white")
        side_menu.place(x=0, y=100, width=250, height=650)
        left_menu_logo = Label(side_menu, image=self.left_menu_icon)
        left_menu_logo.pack(side=TOP, fill=X)

        # ======== MENU Label ============
        self.menu_label = Label(side_menu, text="MENU", bg="#009688", fg="white", font=(
            "Times New Roman", 20)).pack(side=TOP, fill=X)

        # ======== SIDE MENU ICON ============
        self.side_icon = PhotoImage(file="assets/greater-than.png")

        # ======== Employee Button ============
        employee_btn = Button(side_menu, text="EMPLOYEE", image=self.side_icon, compound=LEFT, pady=10, padx=10,
                              anchor="w", command=self.employee, bd=3, bg="white", cursor="hand2", font=("Times New Roman", 16, "bold")).pack(side=TOP, fill=X)

        # ======== Supplier Button ============
        supplier_btn = Button(side_menu, text="SUPPLIER", image=self.side_icon, compound=LEFT, pady=10, padx=10,
                              anchor="w", command=self.supplier, bd=3, bg="white", cursor="hand2", font=("Times New Roman", 16, "bold")).pack(side=TOP, fill=X)

        # ======== Category Button ============
        category_btn = Button(side_menu, text="CATEGORY", image=self.side_icon, compound=LEFT, pady=10, padx=10,
                              anchor="w", bd=3, bg="white", cursor="hand2", font=("Times New Roman", 16, "bold")).pack(side=TOP, fill=X)

        # ======== Product Button ============
        sales_btn = Button(side_menu, text="PRODUCT", image=self.side_icon, compound=LEFT, padx=10, pady=10,
                           anchor="w", bd=3, bg="white", cursor="hand2", font=("Times New Roman", 16, "bold")).pack(side=TOP, fill=X)

        # ======== Sales Button ============
        sales_btn = Button(side_menu, text="SALES", image=self.side_icon, compound=LEFT, padx=10, anchor="w",
                           pady=10, bd=3, bg="white", cursor="hand2", font=("Times New Roman", 16, "bold")).pack(side=TOP, fill=X)

        # ======== Exit Button ============
        exit_btn = Button(side_menu, text="EXIT", image=self.side_icon, compound=LEFT, padx=10, pady=10, anchor="w",command=self.exit,
                          bd=3, bg="white", cursor="hand2", font=("Times New Roman", 16, "bold")).pack(side=TOP, fill=X)

        # ========== Content Data =============
        self.employee_label = Label(
            self.window, text="Total Employees \n[ 0 ]", bg="#33bbf9", fg="white", bd=5, relief=RIDGE, font=("Tohama", 20, "bold"))
        self.employee_label.place(x=300, y=120, height=170, width=350)

        self.supplier_label = Label(
            self.window, text="Total Supplier \n[ 0 ]", bg="#ff5722", fg="white", bd=5, relief=RIDGE, font=("Tohama", 20, "bold"))
        self.supplier_label.place(x=700, y=120, height=170, width=350)

        self.category_label = Label(
            self.window, text="Total Category \n[ 0 ]", bg="#009688", fg="white", bd=5, relief=RIDGE, font=("Tohama", 20, "bold"))
        self.category_label.place(x=1100, y=120, height=170, width=350)

        self.product_label = Label(
            self.window, text="Total Products \n[ 0 ]", bg="#607d8b", fg="white", bd=5, relief=RIDGE, font=("Tohama", 20, "bold"))
        self.product_label.place(x=300, y=350, height=170, width=350)

        self.sales_label = Label(
            self.window, text="Total Sales \n[ 0 ]", bg="#ffc107", fg="white", bd=5, relief=RIDGE, font=("Tohama", 20, "bold"))
        self.sales_label.place(x=700, y=350, height=170, width=350)

        # ======= Footer =============
        footer_label = Label(self.window, text="IMS - Inventory Management System | Developed By Mohammad Arsalan Rather\nFor any Technical Issue Contact: 7780xxxx46",
                             bg="#4d636d", fg="white", font=("Times New Roman", 12, "bold")).pack(side=BOTTOM, fill=X)

    ################################################################################################################################################################################################################################################
    def employee(self):
        self.new_window = Toplevel(self.window)
        self.employee_class_obj = EmployeeClass(self.new_window)

    def supplier(self):
        self.new_window = Toplevel(self.window)
        self.supplier_class_obj = SupplierClass(self.new_window)
        
    def exit(self):
        choice = messagebox.askyesno("Exit","Are you sure you want to exit?")
        if choice:
            self.window.destroy()

if __name__ == "__main__":
    window = Tk()
    IMS = InventoryManagementSystem(window)
    window.mainloop()
