import math

startNum = int(input("Starting Number: "))
endNum = int(input("Ending Number: "))

print(f"Prime nums in range of {startNum} to {endNum} are:  ")
for num in range(startNum, endNum + 1):
    if num > 1:
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                break
        else:
            print(f"{num}", end=" ")
