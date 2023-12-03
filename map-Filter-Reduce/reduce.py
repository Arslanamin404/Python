from functools import reduce
# reduce function reduces a list to single value
nums = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x+y, nums)
print(nums)
print(f"Sum of numbers: {sum}")

square = list(map(lambda x: x**2, nums))
sumSquares = reduce(lambda x, y: x+y, square)
print(f"Sum of Squares: {sumSquares}")
