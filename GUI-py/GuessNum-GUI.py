from tkinter import *
from tkinter import messagebox
import random


class NumberGuessGame:
    def __init__(self):
        # heading1
        self.head1 = Label(text="Welcome to the Number Guessing Game!",
                           font=("Arial", 14, "bold"),
                           bg="light yellow",
                           fg="Purple")
        self.head1.grid(row=0, column=0, columnspan=2)
        # heading2
        self.head2 = Label(text="In this game you have to\nGuess a Number between 0 - 100.",
                           font=("Arial", 12),
                           pady=10,)
        self.head2.grid(row=1, column=0, columnspan=2)

        # stat game
        self.start_new_game()

        # label for guess
        self.num_label = Label(text="Enter your Guess: ",
                               font=("Arial", 12, "bold"),
                               padx=10,
                               fg="#001F3F",
                               bg="#D0FFC2")

        # Align to the left (west)
        self.num_label.place(x=0, y=100)

        self.userNumber = IntVar()
        # input field for guess
        self.user_num = Entry(textvariable=self.userNumber,
                              font=("Arial", 14, "bold"), width=10)
        # Bind the <Return> key event to the check_on_enter method
        self.user_num.bind('<Return>', self.check_on_enter)
        self.user_num.place(x=170, y=100)

        # Reset button
        self.reset_btn = Button(text="Reset / Play-Again",
                                bg="RED",
                                font=("Arial", 12, "bold"),
                                fg="white",
                                command=self.restart_game)
        self.reset_btn.place(x=40, y=150)

        # check_guess button
        self.btn = Button(text="Check Guess",
                          bg="#001F3F",
                          font=("Arial", 12, "bold"),
                          fg="white",
                          command=self.check)
        self.btn.place(x=200, y=150)

        # result
        self.result = Label(text="Result",
                            font=("Open Sans", 12, "bold"),
                            padx=10)
        self.result.place(x=30, y=200)

        self.admin = Label(text="©️Mohammad Arsalan Rather",
                           padx=10)
        self.admin.place(x=100, y=300)

    def start_new_game(self):
        self.gamenum = random.randint(1, 100)
        self.attempts = 1
        print(self.gamenum)

    def restart_game(self):
        self.start_new_game()
        self.user_num.delete(0, END)
        self.result["text"] = "Result "
        self.result["fg"] = "black"
        
        

    def check(self):
        try:
            usernum = int(self.user_num.get())
        except ValueError:
            messagebox.showerror("Value Error!","Invalid Input Please Enter a Valid Integer between 0 to 100.")
        except Exception as err:
            errmsg = f"Error! Something unexpected occurred: {err}"
            messagebox.showerror("Error!",errmsg)
        else:
            if usernum == self.gamenum:
                self.result["text"] = f"Congratulations✅!\n You Guessed it right in {self.attempts} attempts."
                self.result["fg"] = "green"
            elif usernum > self.gamenum:
                self.result["text"] = f"Wrong❌! Try again some smaller values."
                self.result["fg"] = "orange"
                self.attempts += 1
            elif usernum < self.gamenum:
                self.result["text"] = f"Wrong❌! Try again some larger values."
                self.result["fg"] = "red"
                self.attempts += 1

    def check_on_enter(self, event):
        # Call the check method when Enter key is pressed
        self.check()


if __name__ == "__main__":
    window = Tk()
    window.geometry("400x400")
    window.config(bg="light grey")
    window.maxsize(400, 400)
    window.minsize(400, 400)
    window.propagate(0)
    window.title("NumeroQuest - Unleash Your Inner Psychic")
    window.iconbitmap("assets\\number_game_icon.ico")
    game = NumberGuessGame()
    window.mainloop()
