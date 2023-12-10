from playsound import playsound
import time
import os


def ring_alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # seconds to minutes
        seconds_left = time_left % 60  # remaining decimals from minutes to seconds

        os.system("cls")
        print(f"Alarm will sound in {minutes_left:02d}:{seconds_left:02d}")

    os.system("cls")
    print("Time's Up🌄⌛")
    playsound("alarm_sound.mp3")


if __name__ == "__main__":
    mins = int(input("How many minutes until your alarm? Please enter minutes: "))
    secs = int(input("How many seconds until your alarm? Please enter seconds: "))
    total_secs = mins*60 + secs
    ring_alarm(total_secs)
