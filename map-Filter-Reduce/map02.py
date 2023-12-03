# Given a list of floating point numbers use map to calculate the square root of each number as store the result in new list
import math
floating_numbers = [1.2, 3.4, 5.6, 7.8, 9.0, 0.5, 1.0, 1.5, 2.0, 2.5]
square_root = list(map(lambda x: round(math.sqrt(x), 3), floating_numbers))
#! round(math.sqrt(x), 3) ===> this will print only 3 decimal numbers of square root

print(f"Floating_Numbers List: {floating_numbers}")
print(f"Square_Root List: {square_root}")
