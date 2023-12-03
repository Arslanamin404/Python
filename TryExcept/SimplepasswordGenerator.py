import random



def generatePassword(length):
    chars = 'qwertyuioplkjhgfdsazxcvbnmMNBVCXZAQWSDERFGTYHJUIKLOP1234567890!@#$%^&*()?/'
    password = ''
    for i in range(length):
        password += chars[random.randint(0, len(chars))]

    print(f"Your Password: {password}")


try:
    user_len = int(input("Enter length: "))
    generatePassword(user_len)
except ValueError:
    print("Error: NAN! Please enter a valid integer")
except IndexError:
    print("Error: Please enter a valid range")
except Exception as e:
    print(f"Something unexpected occurred: {e}")
