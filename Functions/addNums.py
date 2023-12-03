def addNums(a, b):
    print("Sum of", a, "and", b, "is", a + b)


def isGreater(a, b):
    if a > b:
        print(a, "is greater")
    else:
        print(b, "is greater")


if __name__ == '__main__':
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))

    addNums(num1, num2)
    isGreater(num1, num2)
