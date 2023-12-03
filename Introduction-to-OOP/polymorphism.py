# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the
# same name that can be executed on many objects or classes. Polymorphism is often used in Class methods, where
# we can have multiple classes with the same method name.

class Account:
    def __init__(self, Balance):
        self.balance = Balance

    def calculate_interest(self):
        pass


class SavingAccount(Account):
    def calculate_interest(self):
        return 0.03 * self.balance  # 3% Interest Rate for saving account


class CheckingAccount(Account):
    def calculate_interest(self):
        return 0.05 * self.balance  # 5% Interest Rate for Checking Account


class CurrentAccount(Account):
    def calculate_interest(self):
        return 0.01 * self.balance  # 1% Interest Rate for Current Account


class FixedDepositAccount(Account):
    def calculate_interest(self):
        return 0.10 * self.balance  # 10% Interest Rate for Fixed Deposit Account


amount = int(input("Deposit Amount: "))
saving_account = SavingAccount(amount)
checking_account = CheckingAccount(amount)
current_account = CurrentAccount(amount)
fixed_deposit_account = FixedDepositAccount(amount)


print("------------------------------------------------------")
print(f"If You invest {amount} rupees for 1 Year: ")
print("------------------------------------------------------")
# Polymorphism interest calculator
print(f"Saving Account Interest @3%: {saving_account.calculate_interest()} rupees.")
print(f"Checking Account Interest @5%: {checking_account.calculate_interest()} rupees.")
print(f"Current Account Interest @1%: {current_account.calculate_interest()} rupees.")
print(f"Fixed Deposit Account Interest @10%: {fixed_deposit_account.calculate_interest()} rupees.")
print("------------------------------------------------------")
