import calendar

try:
    year = int(input("Enter year: "))
    for i in range(1, 13):
        print(calendar.month(year, i))
except ValueError:
    print("Please enter a valid integer!")
