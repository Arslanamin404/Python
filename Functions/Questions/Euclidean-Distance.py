# WAP to find the Euclidean distance between two coordinates.
# formula = root{(x2-x1)^2 + (y2-y1)^2}

from math import sqrt

def calculate_Euclidean_distance(x1,x2,y1,y2):
    print(f"A = ({x1},{y1})")
    print(f"B = ({x2},{y2})")
    print(f"Distance between A({x1},{y1}) and B({x2},{y2}) is: {round(sqrt((x2-x1)**2 + (y2-y1)**2), 3)} units")    



print("Welcome to the Euclidean distance calculator!\n")
print("------------------------------------------------------")
try:
    x1 = float(input("Enter x1 coordinate: "))
    y1 = float(input("Enter y1 coordinate: "))
    print("------------------------------------------------------")
    x2 = float(input("Enter x2 coordinate: "))
    y2 = float(input("Enter y2 coordinate: "))
except ValueError:
    print("Invalid Input! Please enter a valid integer value")
except Exception as err:
    print(f"Error! Something unexpected occurred: {err}")
else:
    print("------------------------------------------------------")
    calculate_Euclidean_distance(x1,x2,y1,y2)
    print("------------------------------------------------------\n")