"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

divisors = []


def findDivisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    print(f'Divisors of {n} are: {divisors}')


if __name__ == '__main__':
    num = int(input("Enter number: "))
    findDivisors(num)
