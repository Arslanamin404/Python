name = ""
# while name == "":
#     name = input("Enter your name: ")

while len(name) == 0:
    name = input("Enter your name: ")

print("Welcome, " + name)
i = 1
while i <= 5:
    print(i)
    i += 1

print("\nDecrementing Loop: ")
j = 5
while j > 0:
    print(j)
    j -= 1

# Else can be also used with while loop
k = -5
while k > 0:
    print(k)
    k -= 1
else:
    print("hello guys")
