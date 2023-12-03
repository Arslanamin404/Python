# Extract username from a given email. 
# E.g., if the email is xyz123@gmail.com then the username should be xyz123

email = input("Enter email: ")
username = email.split("@")
print(f"Username : {username[0]}")
