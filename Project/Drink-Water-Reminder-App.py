import time
from plyer import notification
import pyttsx3


def read_notification(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # speed
    engine.say(message)
    engine.runAndWait()


def drink_water_reminder():
    while True:
        time.sleep(3600)  # Wait for 1 hour before the next reminder
        notification.notify(
            title="Hydration Reminder🥛",
            message="Heyy there! It's time to give your body a sip of refreshment. Grab your water bottle and take a moment to hydrate.💦💧",
            timeout=10)  # Display for 10 seconds

    # call read notification function
    read_notification(
        "Hey there! It's time to give your body a sip of refreshment. Grab your water bottle and take a moment to hydrate.")


if __name__ == "__main__":
    drink_water_reminder()
