startNum = int(input("Starting Number: "))
endNum = int(input("Ending Number: "))

print(f"Armstrong numbers in range of {startNum} to {endNum} are:  ")
for num in range(startNum, endNum + 1):
    temp = num
    cubeSum = 0
    while temp != 0:
        lastDigit = temp % 10
        cubeSum += lastDigit ** 3
        temp //= 10
    if cubeSum == num:
        print(num, end="\t")
