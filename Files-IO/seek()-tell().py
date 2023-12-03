# seek() and tell() function
with open("myFile.txt", "r") as f:
    # Moves cursor to the 11th byte in file
    f.seek(11)
    # returns the current position of the cursor in file
    print(f"Current Cursor Position: {f.tell()}th byte")
    # This will read only next 9 bytes from current cursor position
    print(f.read(9))
    # this will read the file from current cursor position to EOF
    # print(f.read()) 
