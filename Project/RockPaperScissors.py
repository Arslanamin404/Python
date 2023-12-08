import random
import time
import sys


def cpuChoice():
    RSP = ["rock", "paper", "scissor"]
    return random.choice(RSP)


def run_game():
    total_game_rounds = 5
    userScore = cpuScore = 0
    current_round = 1
    print("\nWelcome to Rock,Paper & Scissor Game! You have to earn 5 points to exit the game")
    userName = input("Please enter your name: ")

    while current_round <= total_game_rounds and current_round <= total_game_rounds:
        print("\n----------------------------------------\n")
        print(f"\t\tRound: {current_round}")
        print("\n----------------------------------------")

        cpu = cpuChoice()
        userChoice = input(
            "\nEnter your choice [rock,paper,scissor]: ").lower()
        if userChoice not in ['rock', 'paper', 'scissor']:
            print("\nInvalid Choice! Please enter rock, paper or scissor.\n")
            continue
        else:
            current_round += 1
        print("--------------------------------")
        if userChoice == cpu:
            print(userName, ":", userChoice)
            print("CPU:", cpu)
            print("Its a Tie")
            print("User Score:", userScore, " CPU Score:", cpuScore)
        elif (
            (userChoice == "rock" and cpu == "scissor")
            or (userChoice == "scissor" and cpu == "paper")
            or (userChoice == "paper" and cpu == "rock")
        ):
            print(userName, ":", userChoice)
            print("CPU:", cpu)
            print("You won!")
            userScore += 1
            print("User Score:", userScore, " CPU Score:", cpuScore)
        else:
            print(userName, ":", userChoice)
            print("CPU:", cpu)
            print("CPU won!")
            cpuScore += 1
            print("User Score:", userScore, " CPU Score:", cpuScore)

    print("\n\n-----------------------------------------------")
    print("\tUser Score:", userScore, "points")
    print("\tCpu Score:", cpuScore, "points")
    print("-----------------------------------------------")
    if userScore > cpuScore:
        print("\t" + userName.upper(), "won this Game")
    elif userScore < cpuScore:
        print("\tCPU won this Game")
    else:
        print("\tIts a Tie")
    print("-----------------------------------------------\n")

    time.sleep(1)

    print("\n\nDo you want to Play Again? \n")
    while True:
        exit_choice = input("Please enter Y for Yes and Q to Quit: ").lower()
        if exit_choice not in ['y', 'q']:
            continue
        else:
            break

    if exit_choice == 'y':
        print("\nWelcome Back\n")
        return run_game()
    else:
        print("\n🥳🥳🥳🥳")
        print("Thank you for playing!")
        print("We will be waiting for you\n")
        sys.exit("Bye!👋")


if __name__ == "__main__":
    run_game()
