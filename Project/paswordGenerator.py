import random
import string


def generatePassword(length, alpha, numeric, special):
    chars = string.ascii_letters if alpha else ''  # string.ascii_letters prints all the upper and lower case alphabets
    nums = string.digits if numeric else ''  # string.digits prints 0-9 nums
    sp_chars = string.punctuation if special else ''
    password = ''

    # Combine the character sets
    all_chars = chars + nums + sp_chars

    # Check if at least one character set is selected
    if not all_chars:
        print("Please select at least one character set.")
        return

    for i in range(length):
        password += random.choice(all_chars)
    return password


if __name__ == '__main__':
    try:
        print(
            "Welcome to Password Generator, in this program you will be able to generate your most secure passwords.\n")
        passwordLength = int(input("Enter the required length of password: "))
        if passwordLength:
            print("\nDo you want to include Upper/Lowercase letters in your password?")
            isAlpha = int(input("Enter 1 for yes or 0 for No [1/0]: "))
            print("\nDo you want to include Numbers in your password?")
            isNumeric = int(input("Enter 1 for yes or 0 for No [1/0]: "))
            print("\nDo you want to include special characters in your password?")
            isSpecial = int(input("Enter 1 for yes or 0 for No [1/0]: "))

            print("\n----------------------------------------------------------------------------------")
            print(f"\t\tYour password: {generatePassword(passwordLength, isAlpha, isNumeric, isSpecial)}")
            print("-----------------------------------------------------------------------------------")
        else:
            print("Please enter a valid password length")
    except ValueError:
        print("Error: NAN! Please enter a valid Integer. . .")
    except IndexError:
        print("Error: Please enter a valid Range. . .")
    except Exception as err:
        print(f"Something unexpected occurred: {err}")
