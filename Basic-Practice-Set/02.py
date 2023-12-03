# Write a Python program that accepts the user's first and last name and 
# prints them in reverse order with a space between them.

f_name = input("First name: ")
l_name = input("last name: ")

print(f"Reverse: {l_name[::-1]} {f_name[::-1]}")