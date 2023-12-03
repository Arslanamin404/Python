import time

currentTime = time.strftime("%I:%M:%S %p")
currentHour = int(time.strftime("%I"))
print(" ---------------------------")
print("| Current Time:", currentTime, "|")
print(" ---------------------------")

if currentHour < 12:
    print("Good Morning")
elif currentHour == 0:
    print("Mid Night [Good Night]")
elif currentHour == 12:
    print("Good After Noon")
elif currentHour > 12 and currentHour <= 16:
    print("Good Evening")
else:
    print("Good Night")
