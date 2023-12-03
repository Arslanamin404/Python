# Reading a file
f = open('myFile.txt', 'r')
text = f.read()
print(text)
f.close()

# Writing a file
wF = open('writeFile.txt', 'w')
wF.write('Hello World! This text has been written to this file using py script. . .')
wF.close()

"""
# Appending a file
wF = open('writeFile.txt', 'w')
wF.write('\nHello World Again! This text has been appended to this file using py script . . .')
wF.close()
"""
