import os

if not os.path.exists("100 Days of Code"):
    os.mkdir("100 Days of Code")

flag = True

for i in range(100):
    if not os.path.exists(f"100 Days of Code/Day {i + 1}"):
        flag = False
        os.mkdir(f"100 Days of Code/Day {i + 1}")

if flag:
    print("Folders already exist. . .")

"""
# Here, folders will contain the list of directories that are present in given directory
folders = os.listdir("100 Days of Code")
for folder in folders:
    print(folder)
    print(os.listdir(f"100 Days of Code/{folder}"))
"""

# lets get current working directory(CWD)
cwd = os.getcwd()
print(f"Current Working Directory ---> {cwd}")
