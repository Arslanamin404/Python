# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import datetime

# Get user input for the start date
start_date_str = input("Enter the start date (DD-MM-YYYY): ")
start_date = datetime.strptime(start_date_str, "%d-%m-%Y")

# Get user input for the end date
end_date_str = input("Enter the end date (DD-MM-YYYY): ")
end_date = datetime.strptime(end_date_str, "%d-%m-%Y")

# Calculate the difference between the two dates
difference = end_date - start_date

# Extract the number of days from the difference
difference_in_days = difference.days

print("The difference between the two dates is", difference_in_days, "days.")
