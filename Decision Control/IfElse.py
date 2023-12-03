age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to drive")
elif age == 17:
    print("You can apply for learning license")
elif age > 5:
    print("You are not eligible to drive. Have patience. . .")
else:
    print("Invalid age. Please enter a valid age")
