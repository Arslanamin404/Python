def factorial(num):
    fact = i = 1
    while i <= num:
        fact *= i
        i += 1
    return fact


if __name__ == '__main__':
    userinput = int(input("Enter number: "))
    print("Factorial of", userinput, "is", factorial(userinput))
