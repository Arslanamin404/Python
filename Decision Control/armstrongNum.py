num = int(input("Enter number: "))
temp = num
sumCube = 0

while temp != 0:
    lastDigit = temp % 10
    sumCube += (lastDigit ** 3)
    temp = temp // 10

if sumCube == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
