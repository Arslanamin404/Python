# Default function arguments
def name(fName, mName="Johns", lName="clove"):
    print(fName + " " + mName + " " + lName)


name("Mr")  # default arguments will be passed
name("Michel", "John", "dean")  # Default arguments will be ignored
name("Steve", "den")  # Default arguments will be ignored


# required arguments
def avg(a, b):
    return (a + b) / 2


print(avg(12, 65))  # we cannot skip any argument here
print(avg(10, 6))  # we cannot skip any argument here
