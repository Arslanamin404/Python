dictionary = {
    "Happy": "Feeling pleasure or contentment",
    "Cat": "A small domesticated carnivorous mammal",
    "Book": "A physical or digital publication with pages of text or images",
    "Sun": "The star at the center of our solar system that provides light and heat to Earth",
    "Sleep": "A natural recurring state of rest for the body and mind"
}

# print(dictionary["Happy"])
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())
# for key, value in dictionary.items():
#     print(f"\nMeaning of {key} is {value}")


print("Enter the word from the list to get its meaning: ")
i = 1
for keys in dictionary:
    print(f" {i}). {keys}", end=" ")
    i += 1

userInput = input("\n\nEnter word to search: ").title()
print(f"{userInput} : {dictionary[userInput]}")

print("\n-------------------------------------------------------------------------------------------\n")

alien_0 = {'name': 'alien_0', 'color': 'green', 'points': 5}
alien_1 = {'name': 'alien_1', 'color': 'yellow', 'points': 10}
alien_2 = {'name': 'alien_2', 'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    for key, val in alien.items():
        print(f"{key.title()} : {val}")
    print("-------------------")
