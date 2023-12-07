# pip install pyfiglet
from pyfiglet import Figlet

figlet = Figlet(font='speed')

# get all the fonts in list
fonts = figlet.getFonts()

# print all fonts
# for i, font in enumerate(fonts, start=1):
#     print(f"{i} {font}")


user_input = input("Enter Your Text: ")

print(figlet.renderText(user_input))

