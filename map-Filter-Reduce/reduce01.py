# product of list using reduce
import numpy as np
from functools import reduce

nums = list(np.arange(1, 6))
product = reduce(lambda x, y: x*y, nums)
print(f"Product of nums (1-5): {product}")
