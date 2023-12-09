# custom error
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, account_holder_name, initial_amount):
        self.name = account_holder_name
        self.balance = initial_amount

        print(
            f"Account of {self.name} created successfully!\nBalance = ${self.balance:.2f}\n")

    def get_balance(self):
        print(f"Account {self.name} Balance = ${self.balance:.2f}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(
            f"Amount ${amount} Deposited successfully!\nName = {self.name}\nNew Balance = ${self.balance:.2f}\n")

    def is_transaction_feasible(self, amount):
        if amount >= self.balance:
            raise BalanceException(
                f"\nSorry, transaction unsuccessful! Account {self.name} has insufficient funds.\nBalance = ${self.balance:.2f}")
        else:
            return

    def withdraw(self, amount):
        try:
            self.is_transaction_feasible(amount)
            self.balance = self.balance-amount
            print(f"\nWithdrawal Successful!!✅\n${amount} withdrawn.")
            self.get_balance()
        except BalanceException as err:
            print(f"\nWithdraw Interrupted!❌{err}")
        except Exception as e:
            print(f"\nSomething unexpected occurred: {e}")

    def transfer(self, amount, account):
        try:
            print("\n******************************\n\nBeginning Transfer . . .🚀")
            self.is_transaction_feasible(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Money Transferred Successfully✅\n\n******************************\n")
        except BalanceException as err:
            print(f"\nTransfer Interrupted!❌{err}")
        except Exception as e:
            print(f"\nSomething unexpected occurred: {e}")


class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        # 5/100 = 5% ==> deposit amount+5%(deposit) as interest
        self.balance = self.balance+(amount+(amount*(5/100)))
        print(f"Amount ${amount} Deposited successfully!✅")
        print(
            f"Name = {self.name}\nInterest Reward = ${amount*(5/100)}\nNew Balance = ${self.balance:.2f}\n"
        )


# Inheriting SavingsAccount from InterestRewardAccount implies that all savings accounts will have interest reward functionality in addition to basic banking features.The only difference is that interest reward account wont have withdraw fee!
class SavingsAccount(InterestRewardAccount):
    def __init__(self, account_holder_name, initial_amount):
        super().__init__(account_holder_name, initial_amount)
        self.__fee = 5  # on every withdraw their will be $5 fee

    def withdraw(self, amount):
        try:
            self.is_transaction_feasible(amount+self.__fee)
            self.balance = self.balance - (amount+self.__fee)
            print(f"Amount ${amount} withdrawn successfully!✅")
            print(f"Withdrawal Fee = ${self.__fee:.2f}")
            self.get_balance()
        except BalanceException as err:
            print(f"\nWithdrawal Interrupted!❌{err}")
        except Exception as e:
            print(f"\nSomething unexpected occurred: {e}")
