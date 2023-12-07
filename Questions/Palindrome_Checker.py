def check(str):
    if str == str[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")


user_str = input("Enter String: ").lower()
check(user_str)
