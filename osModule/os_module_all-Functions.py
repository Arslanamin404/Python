import os

osFuncs = dir(os)
print("All the Methods/Functions of os module are given below: ")
for index, func in enumerate(osFuncs):
    print(f"{index}). {func}")
