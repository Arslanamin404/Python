# __init__ , __add__, __str__ etc are called magic methods

class Fraction:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    # logic to add 2 fraction numbers
    def __add__(self, other):
        temp_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        temp_denominator = self.denominator*other.denominator
        return "{}/{}".format(temp_numerator, temp_denominator)

    # logic to subtract 2 fraction numbers
    def __sub__(self, other):
        temp_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        temp_denominator = self.denominator*other.denominator
        return "{}/{}".format(temp_numerator, temp_denominator)

    # logic to multiply 2 fraction numbers
    def __mul__(self, other):
        temp_numerator = (self.numerator * other.numerator)
        temp_denominator = (self.denominator*other.denominator)
        return "{}/{}".format(temp_numerator, temp_denominator)

    # logic to divide 2 fraction numbers
    def __truediv__(self, other):
        temp_numerator = (self.numerator * other.denominator)
        temp_denominator = (self.denominator*other.numerator)
        return "{}/{}".format(temp_numerator, temp_denominator)


# if we give this file to anyone and he adds this file to his library folder he will be able to access and all the operations
num1 = Fraction(3, 4)
num2 = Fraction(5, 6)

print("-------------------------------------")
print("Fraction Format n1: ", num1)
print("Fraction Format n2: ", num2)

print("-------------------------------------")
print(f"Add:  {num1} + {num2} = {num1+num2}")
print(f"Subtract:  {num1} - {num2} = {num1-num2}")
print(f"Multiply:  {num1} * {num2} = {num1*num2}")
print(f"Divide:  {num1} / {num2} = {num1/num2}")
print("-------------------------------------")
