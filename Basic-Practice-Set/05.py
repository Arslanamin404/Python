# WAP that will determine the whether when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C), HUMIDITY (%) ==> WEATHER
#* temp >= 30         humidity >=90    Weather ==> Hot and Humid
#? temp >= 30         humidity < 90    Weather ==> Hot
#? temp <30           humidity >= 90   Weather ==> Cool and Humid
#! temp <30           humidity <90     Weather ==> Cool

temp = float(input("Temperature (c): "))
humidity = float(input("Humidity (%): "))

if temp >= 30 and humidity >= 90:
    print("Weather: Hot and Humid")
elif temp >= 30 and humidity < 90:
    print("Weather: Hot")
elif temp < 30 and humidity >= 90:
    print("Weather: Cool and Humid")
else:
    print("Weather: Cool")