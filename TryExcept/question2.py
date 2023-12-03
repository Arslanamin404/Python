"""
Use try except on number guessing game.
Handle the case where thr user enters a non-numeric value
"""
import random

gameNum = random.randint(1, 100)
guess = 1
# print(gameNum)
try:
    while True:
        try:
            userNum = int(input("Enter you guess: "))
            if userNum == gameNum:
                print(f"\nCongratulations!! You guessed it right in {guess} guesses.")
                break
            elif gameNum < userNum:
                print("Try a smaller number\n")
                guess += 1
            else:
                print("Try a greater number\n")
                guess += 1
        except ValueError:
            print("\nError: Please enter a valid integer!\n")
        except Exception as err:
            print(f"An unexpected error has occurred : {err} ")
finally:
    print(f"Thanks for playing! The guess number was {gameNum}")
