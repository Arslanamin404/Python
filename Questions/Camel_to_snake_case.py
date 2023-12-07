str = input("CamelCase: ")

print("Snake_case: ", end="")

for c in str:
    if c.isspace():
        print('_', end="")
    elif c.isupper():
        print(f'_{c.lower()}', end="")
    else:
        print(c, end="")
