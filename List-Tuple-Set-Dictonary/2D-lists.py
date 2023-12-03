drinks = ["coffee", "soda", "tea", "cocktail"]
dinner = ["Pizza", "Burger", "Rice", "Momos", "Pasta", "Waazwan", "Shawarma"]
desert = ["cake", "ice cream", "sweets"]

foodItems = [drinks, dinner, desert]
print(foodItems)
print("---------------------------------")
print(foodItems[0][1])
print("---------------------------------")

for i in range(len(foodItems)):
    for items in foodItems[i]:
        print(items)
    print("\n")

print("---------------------------------")
for items in foodItems[0]:
    print(items)
print("---------------------------------\n")

options = [
    ["Tokyo", "Beijing", "Korea", "Seoul"],
    ["5", "12", "7", "9"],
    ["Ruskin Bond", "Charles Dickens", "Jane Austin", "William Shakespeare"],
    ["Au", "Ag", "Fe", "Gu"],
    ["Venus", "Jupiter", "Mars", "Pluto"],
    ["African Elephant", "Blue Whale", "Giraffe", "Hippo"],
    ["Oxygen", "Florine", "Nitrogen", "Carbon Dioxide"],
    ["Mount Everest", "Mount Fuji", "Mount Kilimanjaro", "Mount Lidwas"],
    ["Pablo Picasso", "Vincent Van Gogh", "Leonardo da Vinci", "John Michel"],
    ["O2", "H2O", "CO2", "NH3"],
]

for i in range(len(options)):
    for j in range(len(options[i])):
        print(options[i][j])
