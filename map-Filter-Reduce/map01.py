# Create a function that takes a list of numbers as strings and converts them into integers using the map function

stringNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']
intNumbers = list(map(lambda x: int(x), stringNumbers))
print(f"String Numbers List: {stringNumbers}")
print(f"Int Numbers List: {intNumbers}")
