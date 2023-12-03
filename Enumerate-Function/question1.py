"""Enumerate a list of nums and print only the even indexed numbers along with their indices"""

nums = [13, 69, 75, 21, 10, 56, 76, 41]
for index, num in enumerate(nums):
    if index % 2 == 0:
        print(f"Index of {num} is {index}.")
