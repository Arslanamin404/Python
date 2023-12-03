import numpy as np

nums = list(np.random.randint(1, 20, size=10))
print("\n--------------------------------------------------------------------------------")
print(f"Original Numbs = {nums}")
print("--------------------------------------------------------------------------------")

# syntax: map(function,iterable)
double = list(map(lambda x: x*2, nums))
print(f"Double Numbs = {double}")
print("--------------------------------------------------------------------------------\n")
