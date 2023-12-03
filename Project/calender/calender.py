import calendar
import time

today = time.strftime("%A %d-%b-%Y")

print("-------------------------------------")
print(f"\tToday: {today}")
print("-------------------------------------")

# CALENDER
try:
    year = int(input("Year [YYYY]: "))
    month = int(input("Month number: "))
    print("------------------")

    calendar = calendar.month(year, month)
    print(calendar)
except ValueError:
    print("Please enter a valid integer!!")
except Exception as err:
    print(f"Something unexpected occurred: {err}")
input("\nPress enter key to exit. . . ")
