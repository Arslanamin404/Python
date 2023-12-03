import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Enter your username: ").lower()
    with open("username.json", "a") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!\n")
else:
    print("Welcome back, " + username + "!")

