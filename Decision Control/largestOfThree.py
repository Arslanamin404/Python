num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num3 and num2 > num1:
    largest = num2
else:
    largest = num3

print("Largest among", num1, num2, num3, "is", largest)
