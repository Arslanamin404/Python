# A constructor in Python is a special method within a class that is automatically called when you create an
# object of that class. It typically initializes the object's attributes or performs any setup needed for the
# object to function properly. In Python, the constructor method is named `__init__`.
class Person():
    def __init__(self, name, occ):
        self.name = name
        self.occupation = occ

    def intro(self):
        print(f"Hey my name is {self.name} and I am a {self.occupation}.")


# a,b,c are objects
a = Person("Mohammad Arsalan Rather", "Python Developer")
b = Person("Victor", "Camper")
c = Person("Sara", "PUBG Character")

a.intro()
b.intro()
c.intro()
