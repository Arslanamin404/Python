class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, student_id, course, semester):
        super().__init__(name, age)
        self.__id = student_id
        self.course = course
        self.sem = semester

    def get_id(self):
        return self.__id

    def display_info(self):
        return f" Name: {self.get_name()}\n Age: {self.get_age()}\n Student_Id: {self.get_id()}\n Course: {self.course}\n Semester: {self.sem}"


Student01 = Student("Mohammad Arsalan Rather", 20, 220538, "BCA", 3)
Student02 = Student("Muneeb Inayat", 19, 220557, "BCA", 3)
Student03 = Student("Sheezan Firdous", 20, 220598, "BTech", 3)

print("-------------------------------------")
print("\tID Card")
print("-------------------------------------")
print(Student01.display_info())
print("\n-------------------------------------")
print("\tID Card")
print("-------------------------------------")
print(Student02.display_info())
print("\n-------------------------------------")
print("\tID Card")
print("-------------------------------------")
print(Student03.display_info())
print("\n------------------------------------------------------\n")
