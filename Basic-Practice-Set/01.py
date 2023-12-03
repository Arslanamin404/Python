# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java

filename = input("Enter File name to obtain its extension: ")
extension = filename.split('.')
print(f"Extension is: {extension[1]}")