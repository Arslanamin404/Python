# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +……. + n/n!
# n will be provided by the user

def factorial(n):
    if n==0 or n ==1:
        return 1
    return n*factorial(n-1)

sum = 0
n = int(input("Enter N: "))
for i in range(1,n+1):
    sum += i/factorial(i)

print(sum)