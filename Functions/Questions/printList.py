def show_players(names):
    i = 1
    for name in names:
        print(f"{i} {name}")
        i += 1


def greet_users(names):
    for name in names:
        print(f"Hello {name}, welcome back!!!")


user_names = ["SmokieFTW", "OmegaFTW", "Rage Fury", "Insane Wolf"]
if __name__ == '__main__':
    while True:
        print("Please Select an Action --->")
        print("1. View layer names\n2. Greet players\n3. Exit\n")
        choice = int(input("Please Enter Your Choice [1/2/3]: "))
        match choice:
            case 1:
                print("List of players: ")
                show_players(user_names)
                print("\n")
            case 2:
                greet_users(user_names)
                print("\n")
            case 3:
                print("Exiting. . .")
                break
            case _:
                print("Invalid Choice, Pleas try again. . .\n")
