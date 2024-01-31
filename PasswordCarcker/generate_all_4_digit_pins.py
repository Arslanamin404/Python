from string import digits
from itertools import product

print(digits)

count = 1
for passcode in product(digits, repeat=4):
    # print(passcode)
    print(*passcode)  # (* is used to unpack iterables)
    count += 1


print("\n----------------------------------")
print(f"Total 4 digit generated pins: {count}")
print("----------------------------------\n\n\n")


# * (* is used to unpack iterables)
l = [1, 2, 3, 5, 6, 17]
print(*l)
