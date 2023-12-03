# Write a program that will check whether the number is Armstrong number or not.

number = int(input("Enter number: "))
temp = number
sum = 0
while temp!=0:
    lastDigit = temp%10
    sum = sum+lastDigit**3
    temp //=10
    
if number == sum:
    print("Armstrong ")
else:
    print("Not Armstrong ")