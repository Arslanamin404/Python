class ATM:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.__menu()
        

    def __menu(self):
        print("How would you like to proceed?")
        print("1. Create Pin")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit\n")

        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            print("Exiting")
        else:
            print("Invalid Choice! Please try again.")

    def create_pin(self):
        self.__pin = input("Enter you 4-digit pin: ")
        if len(self.__pin) == 4:
            print('-----------------------------')
            print("Pin set successfully!")
            print('-----------------------------\n')
        else:
            print('----------------------------------------')
            print("Invalid! Please enter a 4-digit Pin.")
            print('----------------------------------------\n')
        self.__menu()

    def deposit(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the Deposit Amount: "))
            self.__balance += amount
            print("-----------------------------------")
            print("Amount Deposited Successfully!")
            print("-----------------------------------\n")
        else:
            print("--------------")
            print("Invalid Pin!")
            print("--------------\n")
        self.__menu()

    def withdraw(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the Withdrawal Amount: "))
            if amount < self.__balance:
                self.__balance -= amount
                print("-----------------------------------")
                print("Amount withdrawn Successfully!")
                print("-----------------------------------\n")
            else:
                print("-----------------------------------")
                print("Insufficient Balance!")
                print("-----------------------------------\n")
        else:
            print("-------------------")
            print("Invalid Pin!")
            print("-------------------\n")
        self.__menu()

    def check_balance(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            print("-----------------------------")
            print(f"Current Balance: {self.__balance}")
            print("-----------------------------\n")
        else:
            print("-----------------")
            print("Invalid Pin!")
            print("-----------------\n")
        self.__menu()


if __name__ == '__main__':
    JKBank = ATM()
