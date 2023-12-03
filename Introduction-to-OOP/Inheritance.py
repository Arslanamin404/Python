class Animal:
    def __init__(self, name):
        self.name = name


# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} {self.breed} says Woof!"

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} {self.breed} says Meow!"
    
# Creating instances of classes
dog = Dog("Jenny","Husky")
cat = Cat("Whiskers","Calico")

# Accessing Attributes
print("--------------------------------------------------")
print(f"{dog.name} is a {dog.breed}.")
print(dog.speak())
print("--------------------------------------------------")
print(f"{cat.name} is a {cat.breed}.")
print(cat.speak())
print("--------------------------------------------------")