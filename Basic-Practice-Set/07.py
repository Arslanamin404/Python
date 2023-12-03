# Write a program to find the sum of first n numbers, where n will be provided by the user.
# E.g., if the user provides n=10 the output should be 55

n = int(input("N: "))
sum = n*(n+1)//2
print(f"Sum of first {n} numbers is: {sum}")