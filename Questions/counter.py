import time
import winsound


def counter(duration):
    print(f"Countdown Set for {duration} seconds.")
    for i in range(duration, 0, -1):
        print(i,end=" ")
        time.sleep(1)
    print("\n\tTime's Up")
    for i in range(3):
        winsound.Beep(800, 600)
    winsound.Beep(900, 3000)


if __name__ == "__main__":
    try:
        duration = int(input("Enter the countdown duration in seconds: "))
        counter(duration)
    except ValueError:
        print("ERROR: Please enter a valid input for seconds")
