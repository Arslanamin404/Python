#  Write a Python function that takes a sequence of numbers and determines whether all the numbers
# are different from each other.
import numpy as np
def check_nums(nums):
    if len(nums) == len(set(nums)):
        return True
    else:
        return False

numbers = list(np.random.randint(1,100,size=5))
print(numbers)

print(f"\nAll numbers are different: {check_nums(numbers)}")