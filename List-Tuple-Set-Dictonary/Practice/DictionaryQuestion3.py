"""
Make a dictionary containing three major rivers and the country each river runs through.
- Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each country included in the dictionary.
"""

riverCounty = {
    "nile": "egypt",
    "amazon river": "brazil",
    "Yangtze River": "china"
}

for river, country in riverCounty.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n\nRiver")
i = 1
for river in riverCounty.keys():
    print(f"{i}) {river.title()}")
    i += 1

print("\n\nCountry")
i = 1
for country in riverCounty.values():
    print(f"{i}) {country.title()}")
    i += 1
