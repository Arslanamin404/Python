# Raise an error if user enters string other than quit

while True:
    user_num = input("Enter any integer or 'quit' to exit: ").lower()
    if user_num == 'quit':
        print("\nQuiting. . .")
        break
    try:
        int(user_num)
    except ValueError:
        print("Please enter valid integer")
