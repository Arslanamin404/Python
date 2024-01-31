from string import ascii_letters, punctuation, digits
from itertools import product

password = ascii_letters + punctuation + digits

with open("password_list_7chars.txt", "a") as file:
    for new_pass in product(password, repeat=7):
        print(*new_pass)  # this will generate all the possible 7 chars passwords
        file.write("".join(new_pass) + "\n")  # Join the characters and write to the file
