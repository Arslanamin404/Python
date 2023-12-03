# this dict contains emp id and their performance out of 100
empData1 = {
    1000: 49,
    1001: 92,
    1002: 45,
    1003: 69,
    1004: 50,
    1005: 89,
    1006: 98,
    1007: 78
}
empData2 = {
    1008: 15,
    1009: 85,
    1010: 74,
    1011: 98,
    1012: 85
}

# This will update all the key pairs of 2 in 1
empData1.update(empData2)
# print(empData1)

# rest are almost same to set,list,tuple methods

print(" -------------- ")
print("| Emp | Rating |")
print(" -------------- ")
for empId, rating in empData1.items():
    print(f"| {empId} : {rating}%   |")
print(" -------------- ")
