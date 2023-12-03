"""Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and
add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.
# SAMPLE:
Hello [Guest's Name]! Welcome to our marriage event. We're delighted to have you here.
Your visit has been recorded. Enjoy your time with us!
"""
import time


def recordGuest():
    while True:
        current_date_time = time.strftime("%d-%m-%Y %I:%M:%S %p")
        print(f"Current DateTime: {current_date_time}\n")
        name = input("Enter Guest Name or q to exit: ").lower()
        if name == 'q':
            print("\nExiting. . .")
            break
        print(f"Hello, {name.title()}! Welcome to our marriage event. We're delighted to have you here.")
        print("Your visit has been recorded. Enjoy your time with us!\n")

        with open("GuestEntryBook.txt", "a") as file:
            file.writelines(f"{current_date_time} -- {name.title()}! Welcome to our marriage event.\n")


def readGuestRecord():
    with open("GuestEntryBook.txt", "r") as file:
        guest_data = file.read()
        print("\n------------------------------------------------------------------------")
        print("\t\t\t\tList Of Guests")
        print("------------------------------------------------------------------------")
        print(guest_data)


try:
    while True:
        print("\nPlease select an action ----->\n\n1. Add Guests\n2. View Guest Record\n3. Exit\n")
        userChoice = int(input("Enter your choice: "))
        match userChoice:
            case 1:
                recordGuest()
            case 2:
                readGuestRecord()
            case 3:
                print("\nExiting. . .")
                break
            case _:
                print("\nInvalid Choice!\n")
except ValueError:
    print("\nError: Please enter a valid integer")
except Exception as err:
    print(f"\nSomething unexpected occurred: {err}")
