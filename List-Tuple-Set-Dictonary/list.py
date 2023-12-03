# List is same as array in C, C++, Java
import random

marks = [10, 14, 11, 54, 0, 12, 16]
print(type(marks))
print("Length:", len(marks))
print("Max value is", max(marks))
print(random.choice(marks))

print("\n---------------------------------------------\n")

course = ["MCA", "BCA", "BSC", "Diploma", "BTech CSE", "BSc Nursing"]
print("Length:", len(course))

# for i in range(len(course)):
#     print(course[i])
for i in course:
    print(i)

print("\n", course[:])

# same can be done for strings also
if "MCA" in course:
    print("Course is Available\n")
else:
    print("Course is Not Available\n")

# list comprehension
items = [i * i for i in range(1, 11) if i % 2 == 0]
print(items)

"""names = []
num = int(input("\nNum: "))
for i in range(num):
    name = input("Name: ")
    names.append(name)
print("\n----------------\n")
for name in names:
    print(f"Name: {name}")
"""
print("\n----------------------------------\n")


def addItem(items):
    num = int(input("Number of items to add: "))
    for i in range(num):
        item = input(f"Item {i}: ")
        items.append(item)


list_items = []
addItem(list_items)

print("\nList items are: ")
for item in list_items:
    print(item)
