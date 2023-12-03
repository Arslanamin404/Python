# use filter on list of numbers and to return a list containing only the +ve numbers
import numpy as np

numbers = list(np.random.randint(-10, 10, size=12))
positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))
print(f"Original: {numbers}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")
