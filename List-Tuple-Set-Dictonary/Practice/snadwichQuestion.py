"""PART 01" Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty
list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as
I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the
sandwiches have been made, print a message listing each sandwich that was made.

PART 02: Make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of
your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all
occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches
"""


# These are the sandwich orders made by different customers
sandwich_orders = ["Club Sandwich",
                   "Pastrami Sandwich",
                   "Chicken Caesar Wrap",
                   "Turkey and Swiss Sandwich",
                   "Pastrami Sandwich",
                   "Grilled Cheese Sandwich",
                   "Tuna Salad Sandwich",
                   "Veggie Wrap",
                   "Cuban Sandwich",
                   "Pastrami Sandwich",
                   "French Dip Sandwich",
                   ]

finished_sandwiches = []

print("Sorry, We have run out of Pastrami Sandwich. . .\n")

while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")

i = 1
while sandwich_orders:
    current_Sandwich = sandwich_orders.pop()
    print(f"{i}. I made your {current_Sandwich}.")
    finished_sandwiches.append(current_Sandwich)
    i += 1

print("\nList of finished sandwiches:")
print("-----------------------------")
i = 1
for sandwich in finished_sandwiches:
    print(i, sandwich)
    i += 1
