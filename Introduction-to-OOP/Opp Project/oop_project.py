from bank_accounts import *

Arsalan = BankAccount("Mohammad Arsalan Rather", 1500)
Victor = BankAccount("Victor", 500)
Sara = BankAccount("Sara", 200)

Arsalan.get_balance()
Victor.get_balance()
Sara.get_balance()

Arsalan.deposit(1000)
Victor.deposit(200)
Sara.deposit(100)

Arsalan.withdraw(500)
Victor.withdraw(2500)

Arsalan.transfer(150000, Sara)
Arsalan.transfer(150, Sara)

khan = InterestRewardAccount("Khan", 1000)
khan.deposit(100)
khan.withdraw(200)
khan.transfer(300, Arsalan)

John = SavingsAccount("John", 500)
John.deposit(1000)
John.withdraw(300)


