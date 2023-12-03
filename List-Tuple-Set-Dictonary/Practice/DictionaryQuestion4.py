"""Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person. Loop through the dictionary, and print
each person’s name and their favorite places"""

# these names and places are from PUBG
favPlaces = {
    "Victor": "Severny",
    "Carlo": "Pochinki",
    "Sara": "Military Base",
    "Andi": "George Pool"
}

for key, value in favPlaces.items():
    print(f"{key}'s favorite place is {value}.")
