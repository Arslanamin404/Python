# String Methods
name = "   mohammad arsalan rather  "
name = name.strip()  # removes the extra white spaces from both sides
print("Length: ", len(name))
print("Index of o is", name.find("o"))
print("UPPERCASE:", name.upper())
print("lowercase:", name.lower())
print("Title Case:", name.title())  # capitalizes first letter of each word
print("isDigit:", name.isdigit())
print("isAlpha:", name.isalpha())
print("Count 'e':", name.count("e"))
print("Replace 'a':", name.replace("a", "m"))
print("Print my name 2 times:\n", name * 2)
