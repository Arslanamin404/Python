from tkinter import *


class FactorialWindow:
    def __init__(self):
        self.label = Label(text="Enter a number: ",
                           font=("Arial", 14),
                           fg="purple",
                           bg="light yellow")
        self.label.grid(row=1, column=0)

        self.value = IntVar()
        self.number = Entry(textvariable=self.value,
                            font=("Arial", 14),
                            fg="red",
                            width=10)
        self.number.grid(row=1, column=1)

        self.factorial_btn = Button(text="Check Factorial",
                                    font=("Arial", 12, "bold"),
                                    bg="#5b5b5b",
                                    fg="white",
                                    command=self.factorial)
        self.factorial_btn.place(x=30, y=50)

        self.reverse_btn = Button(text="Reverse",
                                  font=("Arial", 12, "bold"),
                                  bg="#5b5b5b",
                                  fg="white",
                                  padx=10,
                                  command=self.reverse)

        self.reverse_btn.place(x=190, y=50)

        self.result = Label(text=" Result ",
                            font=("Arial", 14, "bold"),
                            fg="white",
                            bg="purple",
                            padx=10,
                            pady=10)
        self.result.place(x=10, y=120)

    def factorial(self):
        num = int(self.number.get())
        originalVal = num
        fact = 1
        while (num != 0):
            fact = fact*num
            num -= 1
        self.result["text"] = f"Factorial of {originalVal} is {fact}."

    def reverse(self):
        num = int(self.number.get())
        originalVal = num
        rev = 0
        while (num != 0):
            lastDigit = num % 10
            rev = (rev*10)+lastDigit
            num //= 10
        self.result["text"] = f"Reverse of {originalVal} = '{rev}'."


window = Tk()
window.geometry("400x400")
window.maxsize(600, 600)
window.minsize(400, 400)
window.title("Find Factorial of Number!")

factorial_window = FactorialWindow()

window.mainloop()
