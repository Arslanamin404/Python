class Person:
    def __init__(self):
        self.__name = ""  # Initialize the private name attribute
        self.__age = 0   # Initialize the private age attribute

    @property
    def name(self):
        # Getter method for name
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 4:
            # Setter method for name
            self.__name = new_name
        else:
            print("Please enter a valid name!")

    @property
    def age(self):
        # Getter method for age
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            # Setter method for age
            self.__age = new_age
        else:
            print("Please enter a valid age!")

    def info(self):
        # Method to print user info
        print(f"My name is {self.__name} and I am {self.__age} years old.")


if __name__ == "__main__":
    user1 = Person()

    # Using setter methods to set name and age
    user1.name = "Arsalan"
    user1.age = 20

    # Using getter methods to access name and age
    print("------------------------------")
    print(f"Name: {user1.name}")
    print(f"Age: {user1.age}")
    print("------------------------------")
    # Displaying user info
    user1.info()
