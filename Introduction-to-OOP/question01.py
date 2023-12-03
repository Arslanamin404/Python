#  Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#! Make a method called describe_restaurant() that prints these two pieces of  information, and a method called
#! open_restaurant() that prints a message indicating that the restaurant is open.
# ? Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant_1 = Restaurant("Gourmet Fusion Bistro", "Fusion")
restaurant_2 = Restaurant("Mama Mia Trattoria", "Italian")
restaurant_3 = Restaurant("Spice Kingdom Indian Cuisine", "Indian")
restaurant_4 = Restaurant("Sushi Sensation", "Japanese")

# print("Restaurant Name: ", restaurant_1.restaurant_name)
# print("Cuisine Type: ", restaurant_1.cuisine_type)

print("----------------------------------------------------------------------------------------------")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print("----------------------------------------------------------------------------------------------")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
print("----------------------------------------------------------------------------------------------")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
print("----------------------------------------------------------------------------------------------")
restaurant_4.describe_restaurant()
restaurant_4.open_restaurant()
print("----------------------------------------------------------------------------------------------")
