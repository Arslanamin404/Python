def printMultiplicationTable(num):
    print("Table of ", num)
    for i in range(1, 11):
        print(num, "X", i, "=", num * i)


if __name__ == '__main__':
    userInput = int(input("Enter number: "))
    printMultiplicationTable(userInput)
