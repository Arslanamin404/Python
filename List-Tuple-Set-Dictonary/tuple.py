a = (1, 35, 45)
print(type(a))
print(a[2])

print("-----------------------")

if 45 in a:
    print("Yes 45 is Present")
else:
    print("Not Present")


print("\n-----------------------\n\tNAMES\n-----------------------")
names = ("Smokie", "Omega", "Mortal", "Scout")
for name in names:
    print(name)


menu = (
    "Shawarma",
    "Momos",
    "Biryani",
    "Tandoori Chicken",
    "Grilled Chicken",
    "Afghani Chicken",
)

print("\n-----------------------\n\tMENU\n-----------------------")
for item in range(len(menu)):
    print(menu[item])

print("-----------------------")
