def factorial(n):
    """
    this function takes n and returns the factorial of n using
    recursion.
    fact(n) = n*fact(n-1)
     """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


user_input = int(input("Enter number: "))
print(f"Factorial of {user_input} is {factorial(user_input)}")
