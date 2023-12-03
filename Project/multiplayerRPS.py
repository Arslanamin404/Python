import os


def get_player_choice(player_name):
    choice = input(f"{player_name}'s turn: ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'rock,' 'paper,' or 'scissors.'\n")
        choice = input(f"{player_name}'s turn: ").strip().lower()
    return choice


try:
    print("####################################################################################################")
    print("\t\t\t\tRock-Paper-Scissors Game")
    print("####################################################################################################")
    p1 = input("Enter Player 1's name: ").title()
    p2 = input("Enter Player 2's name: ").title()

    exit_choice = 1
    while exit_choice:
        # cls works only for windows and clear works for linux,mac
        os.system("cls" if os.name == 'nt' else 'clear')
        print("############################################################################################################")
        print("\tEnter your choice [Rock, Paper, Scissors] to win this game. Best of luck to both of you!")
        print(
            "############################################################################################################")
        p1_choice = get_player_choice(p1)
        p2_choice = get_player_choice(p2)

        if p1_choice == p2_choice:
            print("#############################################################################################")
            print("\t\t\t\tIt's a Tie!!!")
            print("#############################################################################################\n")
        elif (
                (p1_choice == 'rock' and p2_choice == 'scissors') or
                (p1_choice == 'scissors' and p2_choice == 'paper') or
                (p1_choice == 'paper' and p2_choice == 'rock')
        ):
            print("#############################################################################################")
            print(f"\t\t\t\t\t{p1} wins!")
            print("#############################################################################################\n")
        else:
            print("#############################################################################################")
            print(f"\t\t\t\t\t{p2} wins!")
            print("#############################################################################################\n")

        exit_choice = int(input("Do you want to play again? Enter 1 to play again and 0 to exit [1/0]: "))
        if not exit_choice:
            print("#############################################################################################")
            print(f"\t\t\t\t\tEXITING...")
            print("#############################################################################################\n")

except ValueError:
    print("\nError: Please enter a valid input (1 or 0) when asked to play again.")
except Exception as err:
    print(f"\nSomething unexpected occurred: {str(err)}!")
