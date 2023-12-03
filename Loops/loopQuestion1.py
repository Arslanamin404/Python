"""A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3,
the ticket is free. if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket."""

numUsers = 0
try:
    numUsers = int(input("Number of people: "))
except ValueError:
    print("Error: Not a number! Please enter a valid integer.")

money = 0
userInfo = {}
try:
    for i in range(numUsers):
        name = input(f"\n{i + 1}. Name: ")  # key
        age = int(input(f"Age of {name}: "))  # value
        userInfo[name] = age
        if age <= 3:
            print("Free Ticket")
        elif 3 < age <= 12:
            print("Ticket Price: $10")
            money += 10
        elif age > 12:
            print("Ticket Price: $15")
            money += 15
        else:
            print("Invalid age entered.")
except ValueError:
    print("Error: Invalid Input! Please enter a valid age.")

print("\n---------------------------")
print("Name   \t:   Ticket Price")
print("---------------------------")
for key, value in userInfo.items():
    print(f"{key.title()}\t: ${value}")

print("\n-------------------------------")
print(f"Total payable amount = ${money}")
print("-------------------------------")
