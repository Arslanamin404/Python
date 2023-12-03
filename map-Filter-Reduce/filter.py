import numpy as np
numbers = list(np.arange(1, 21))

# SYntax: filter(condition,iterable)
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))

print("-------------------------------------------------------------------")
print(f"Original List: {numbers}")
print(f"Even List: {evens}")
print(f"Odd List: {odds}")
print("-------------------------------------------------------------------")
