# Decorators in programming are functions that modify the behavior of other functions or methods.
# They are often used for adding functionality, such as logging or authentication, to existing code.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Welcome to our program!")
        result = func(*args, **kwargs)
        return result
    return wrapper


@my_decorator
def greet(name):
    print(f"Hello {name}! Have a nice time. . .")


@my_decorator
def farewell(name):
    print(f"GoodBye {name}! We hope you enjoyed. . .")


print("-------------------------------------------------")
greet("Mohammad Arsalan Rather")
print("-------------------------------------------------")
farewell("Mohammad Arsalan Rather")
print("-------------------------------------------------")
