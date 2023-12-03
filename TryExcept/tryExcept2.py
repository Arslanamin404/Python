try:
    num = int(input("Enter index: "))
    a = [32, 43, 54, 23, 55, 221]
    print(a[num])
except ValueError as vErr:
    # print(vErr)
    print("Index entered is not an integer")
except IndexError as err:
    print(err)
    # print("Index Error")
