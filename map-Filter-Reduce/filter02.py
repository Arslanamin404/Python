import math


def checkPrime(x):
    if x < 2:
        return False
    for i in range(2, math.isqrt(x)+1):
        if x % i == 0:
            return False
    return True


numbers = [2, 4, 7, 8, 11, 12, 13, 16, 17, 19, 22, 23, 29, 31, 37]

prime = list(filter(checkPrime, numbers))
non_prime = list(filter(lambda x: not checkPrime(x), numbers))

print("Prime numbers:", prime)
print("Non-prime numbers:", non_prime)
