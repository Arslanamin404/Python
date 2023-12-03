"""
Write a python program to translate a message into secret code language. Rules given below to translate English to code language
Coding:
if the word contains at least 3 characters, remove the first letter and append it at the end
  now append three random characters at the starting and the end
else:
  simply reverse the string
Decoding:
if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
Your program should ask whether you want to code or decode
"""

import random
import string


# Define a custom exception class named SpaceNotAllowedError and pass the built in Exception class for inheritance
class SpaceNotAllowedError(Exception):
    def __init__(self):
        # Initialize the custom error message
        self.error = "Enter only one-word messages for more security"
        # Call the constructor of the parent 'Exception class' with the error message
        super().__init__(self.error)



def secret_code(start_chars, end_chars, text):
    code_message = ""
    for _ in text:
        if len(text) >= 3:
            first_char = text[0]
            code_message = start_chars + text[1:] + first_char + end_chars
        else:
            code_message = text[::-1]

    return code_message


def decode(encoded_text):
    decode_text = ""
    for _ in encoded_text:
        if len(decode_text) < 3:
            decode_text = encoded_text[::-1]
        else:
            decode_text = encoded_text[3:-3]
            last_char = decode_text[-1]
            decode_text = last_char + decode_text[:-1]
    return decode_text


message = ""
# this join 3 random char into string
start_randomChars = "".join(random.choice(string.ascii_letters) for _ in range(3))
end_randomChars = "".join(random.choice(string.ascii_letters) for _ in range(3))

try:
    print("Please enter only one word message to make it more secure!!!")
    message = input("Message: ")
    if ' ' in message:
        raise SpaceNotAllowedError()

    code_lang = secret_code(start_randomChars, end_randomChars, message)
    decode_lang = decode(code_lang)
    print(f"\nEncoded: {code_lang}")
    print(f"Decoded: {decode_lang}")

except SpaceNotAllowedError as err:
    print(f"Custom error: {err}")
