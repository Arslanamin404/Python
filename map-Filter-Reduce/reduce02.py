# find max using reduce
import numpy as np
from functools import reduce

nums = list(np.random.randint(1, 50, size=10))
max = reduce(lambda x, y: x if x > y else y, nums)
min = reduce(lambda x, y: x if x < y else y, nums)
print(nums)
print(f"Max Element: {max}")
print(f"Min Element: {min}")
