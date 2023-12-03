for i in range(15):
    if i == 10:
        break
    print("5 X", i + 1, "=", 5 * (i + 1))

print("\nOdd nums from 1 - 10")

for j in range(1, 10):
    if j % 2 == 0:
        continue
    print(j)
