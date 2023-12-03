import pickle
# WAP to store a list of student names in binary file
# pickle module is used handle fileio

numOfStudents = int(input("Number of students: "))
names = []
for i in range(numOfStudents):
    names.append(input(f"Student{i+1} Name: ").title())

with open("studentListBin", "wb") as f:
    # dump(source,destination) method is used to write a binary file
    pickle.dump(names, f)
