# This program is a simple utility for converting integers to different representations.
# The user can choose an option and input an integer to perform the selected conversion.
# Integer to HexaDecimal, Octal and complex
class IntegerConverter:
    def __init__(self):
        self.menu()

    def menu(self):
        print("Hello User! Welcome to this program. Please enter your choice.\n")
        print("1. Integer to Hexadecimal")
        print("2. Integer to Octal")
        print("3. Integer to Complex")
        print("4. Exit\n")

        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
            self.menu()

        if user_input == 1:
            self.__hex__()
        elif user_input == 2:
            self.__oct__()
        elif user_input == 3:
            self.__complex__()
        elif user_input == 4:
            print("Goodbye")
        else:
            print("Invalid Choice")
            self.menu()

    def __hex__(self):
        try:
            num = int(input("Enter number: "))
            print(f"\n>> {num} in Hexadecimal is {hex(num)}.\n")
        except ValueError:
            print("\n>>> Invalid input. Please enter a valid integer.\n")
        # self.menu()

    def __oct__(self):
        try:
            num = int(input("Enter number: "))
            print(f"\n>> {num} in Octal is {oct(num)}.\n")
        except ValueError:
            print("\n>>> Invalid input. Please enter a valid integer.\n")
        # self.menu()

    def __complex__(self):
        try:
            num = int(input("Enter number: "))
            print(f"\n>> {num} in Complex is {complex(num)}.\n")
        except ValueError:
            print("\n>>> Invalid input. Please enter a valid integer.\n")
        # self.menu()


IntegerConverter()
