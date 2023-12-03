import math


def isPrime(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")


if __name__ == '__main__':
    number = int(input("Number: "))
    isPrime(number)
