def printNums(n, index=0):
    if index == len(n):
        return
    else:
        print(n[index])
        printNums(n, index + 1)


nums = [5, 6, 3, 6, 2, 6]
printNums(nums)
