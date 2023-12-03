import time

# strftime() gives us the hour minute and seconds
print("\nCurrent Hour:", time.strftime("%H"))
print("Current Minute:", time.strftime("%M"))
print("Current Second:", time.strftime("%S"))
print("Day:", time.strftime("%A"))
print("Date:", time.strftime("%d"))
print("Month:", time.strftime("%B"))
print("Year:", time.strftime("%Y"))
print("-----------------------------------------------------------------")
print("Current Time [24-Hour]:", time.strftime("%H:%M:%S"))
print("-----------------------------------------------------------------")
print("Current Time [12-Hour]:", time.strftime("%I:%M:%S %p"))
print("-----------------------------------------------------------------")