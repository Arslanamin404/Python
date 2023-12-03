def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end="\t")


UserNum = int(input("Enter number: "))
print(f"Factors of {UserNum} are: ")
factors(UserNum)
