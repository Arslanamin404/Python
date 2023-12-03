# Write a Python program that takes two numbers as input from the user and calculates their division.
# Use a try-except block to handle the case where the second number is zero and print an error message in such a case.
# using Raise keyword
try:
    numerator: float = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    if denominator == 0:
        raise ZeroDivisionError("ERROR: Division by Zero not allowed! IDIOT!")
    result = numerator / denominator
except ZeroDivisionError as ZeroErr:
    print(f"\n{ZeroErr}")
except ValueError:
    print("\nError: NAN! Please enter only numbers")
else:
    print(f"{numerator}/{denominator} = {numerator / denominator}")
