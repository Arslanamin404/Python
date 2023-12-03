"""
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
"""


def make_shirt(size, ts_text):
    print(f"This shirt is of '{size}' size and it has '{ts_text}' printed on it.")


if __name__ == '__main__':
    userSize = input("Size of shirt: ")
    message = input("Message to be printed on the shirt: ").upper()
    make_shirt(userSize, message)
