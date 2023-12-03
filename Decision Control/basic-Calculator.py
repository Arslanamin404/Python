print("\t\tWelcome to the Basic Python Calculator Program [+,-,*,/]\n")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
operator = input("Enter operator: ")

if operator == "+":
    print("Sum =", num1 + num2)
elif operator == "-":
    print("Difference =", num1 - num2)
elif operator == "*":
    print("Product =", num1 * num2)
elif operator == "/":
    print("Quotient: ", num1 / num2)
else:
    print("Invalid Operator. Please try again. . .")
