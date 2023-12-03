import random


def cpuChoice():
    RSP = ["rock", "paper", "scissor"]
    return random.choice(RSP)


MAXscore = 5
userScore = 0
cpuScore = 0
print("Welcome to Rock,Paper & Scissor Game! You have to earn 5 points to exit the game")
userName = input("Please enter your name: ")
while userScore < MAXscore and cpuScore < MAXscore:
    cpu = cpuChoice()
    userChoice = input("\nEnter your choice [rock,paper,scissor]: ").lower()
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
    elif (
        (userChoice == "scissor" and cpu == "rock")
        or (userChoice == "paper" and cpu == "scissor")
        or (userChoice == "rock" and cpu == "paper")
    ):
        print(userName, ":", userChoice)
        print("CPU:", cpu)
        print("CPU won!")
        cpuScore += 1
        print("User Score:", userScore, " CPU Score:", cpuScore)
    else:
        print("Invalid input. Please try again. . .")

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
