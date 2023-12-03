class Student:
    # static variables ==> make fixed information as static variables so that we can save memory
    __college_name = "Institute of E-sports (IES)"
    __country = "Kashmir"

    def __init__(self, rno, name):
        self.__roll_num = rno
        self.__name = name

    def student_info(self):
        print(f"Name: {self.__name}")
        print(f"Roll Number: {self.__roll_num}")
        print(f"College: {Student.__college_name}")
        print(f"Country: {Student.__country}")


s1 = Student(69, "John Wick")
s2 = Student(57, "Sul Kal")
s3 = Student(87, "Gull Kak")
s4 = Student(88, "Ammi Kak")

print("------------------------------------------")
s1.student_info()
print("------------------------------------------")
s2.student_info()
print("------------------------------------------")
s3.student_info()
print("------------------------------------------")
s4.student_info()
print("------------------------------------------")
