print(
    "Chose conversion type [1 for Celsius to Fahrenheit and 0 for Fahrenheit to Celsius]"
)
choice = int(input("Please enter your choice: "))
if choice == 1:
    celsiusTemp = float(int(input("Temperature in Celsius: ")))
    fahrenheitTemp = (celsiusTemp * (9 / 5)) + 32
    print(celsiusTemp, "C in Fahrenheit is:", fahrenheitTemp, "F")
elif choice == 0:
    fahrenheitTemp = float(int(input("Temperature in Celsius: ")))
    celsiusTemp = (fahrenheitTemp - 32) * (5 / 9)
    print(fahrenheitTemp, "F in Celsius is:", celsiusTemp, "C")
else:
    print("Invalid Choice. Please try again. . .")
