try:
    userNum = int(input("Enter number: "))
    for i in range(1, 11):
        print(f"{userNum} X {i} = {userNum * i}")
except Exception as err:
    print(f"ERROR: {err}")

print("\nRest of code")
print("Some important code")
print("End of code")

try:
    num = int(input("Num: "))
    if num < 5:
        raise ValueError("number must be greater than 5")
    print(num)
except ValueError as e:
    print(e)
