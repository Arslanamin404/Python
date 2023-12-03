# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints  a personalized greeting to the user.

class user():
    def __init__(self, first, last, username, gender, age):
        self.first_name = first
        self.last_name = last
        self.username = username
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, known by their username {self.username}, is a {self.age}-year-old {self.gender}."
              "This brief profile provides a glimpse into their identity, capturing the essence of who they are as an individual.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Welcome to your profile.")


user_01 = user("John", "Smith", "jsmith123", "Male", 30)
user_02 = user("Emily", "Jones", "ejones456", "Female", 25)
user_03 = user("Michael", "Johnson", "mjohnson789", "Male", 35)
user_04 = user("Sarah","Davis", "sdavis101", "Female", 28)
user_05 = user("David", "Anderson", "danderson222", "Male", 40)

print("------------------------------------------------------------------------------------------------------------------------------------")
user_01.greet_user()
user_01.describe_user()
print("------------------------------------------------------------------------------------------------------------------------------------")

user_02.greet_user()
user_02.describe_user()
print("------------------------------------------------------------------------------------------------------------------------------------")

user_03.greet_user()
user_03.describe_user()
print("------------------------------------------------------------------------------------------------------------------------------------")

user_04.greet_user()
user_04.describe_user()
print("------------------------------------------------------------------------------------------------------------------------------------")

user_05.greet_user()
user_05.describe_user()
print("------------------------------------------------------------------------------------------------------------------------------------")