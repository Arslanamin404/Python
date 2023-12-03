with open('myFile.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end="")
