# Finally block is always executed regardless of exception generation.
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cant divide by Zero!!!!")
    else:
        print(f"Quotient: {result}")
    finally:
        print("\nThis block of code will execute always")


try:
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
except ValueError:
    print("Please enter a valid integer")
else:
    divide(num1, num2)
