def fibonacci_Series(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_Series(n - 1) + fibonacci_Series(n - 2)


term = int(input("Enter term: "))
print(f"The {term}th term of Fibonacci Series is {fibonacci_Series(term)}.")
