# Basics
class Person:
    name = "Mohammad Arsalan Rather"
    occupation = 'Developer'
    age = 20

    def info(self):
        print(
            f"'{(self.name).title()}' is '{self.age}' years old and has pursued '{(self.occupation.title())}' course.")


# a,b,c are objects
print("-----------------------------------------------------------------------------------")
a = Person()
a.name = "Victor"
a.occupation = 'camping'
a.age = 69
a.info()

print("-----------------------------------------------------------------------------------")
b = Person()
b.name = "john Wick"
b.occupation = "Acting"
b.age = 36
b.info()

print("-----------------------------------------------------------------------------------")
c = Person()
c.info()
# as no value is assigned to class attributes so it will take default values
print("-----------------------------------------------------------------------------------")
