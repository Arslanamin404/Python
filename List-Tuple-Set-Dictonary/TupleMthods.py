import random

countries = ("Kashmir", "Bahrain", "Pakistan", "Spain", "Germany", "Kuwait")
i = 0
for country in countries:
    print(i, country)
    i += 1
# most of the tuple methods are same
print("\nLength of tuple is:", len(countries))
print("Index of Bahrain is", countries.index("Bahrain"))
