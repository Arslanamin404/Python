Fruits = ["Apple", "Mango", "Pear", "Banana", "PineApple"]
print("---------------------------------------------------------------------------------")
for i, fruit in enumerate(Fruits, start=1):
    print(f"\t{i}. {fruit}", end="\t")

print("\n---------------------------------------------------------------------------------\n")
# for string
name = "Arsalan"
for index, char in enumerate(name):
    print(f"Index of {char} is {index}.")
