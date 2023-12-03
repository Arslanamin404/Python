# Use Map --> List of temperature in celsius and convert them to Fahrenheit using (C*9/5)+32.
temperatures_celsius = [20.5, 25.0, 30.2, 15.8, 10.3,
                        22.7, 18.1, 27.6, 12.4, 29.9]
temperatures_fahrenheit = list(
    map(lambda x: round((x * (9/5) + 32), 3), temperatures_celsius))
print(temperatures_fahrenheit)
