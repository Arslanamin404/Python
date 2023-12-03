# In this syntax you do not need to close the file its done automatically with this syntax.
# We will be suing this syntax


# READ
with open("writeFile.txt", "r") as file:
    content = file.read()
    words = len(content.split(" "))
    print(content)
    print(words)

# WRITE
with open("writeFile.txt", "w") as file:
    file.write("Hello World! This text has been written to this file using py script")

# APPEND
with open("writeFile.txt", "a") as file:
    file.write("\nHello World Again! This text has been appended to this file using py script")
