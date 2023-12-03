import random


def generate_OTP():
    otp = ""
    for i in range(6):
        otp = otp + str(random.randint(1, 9))
    return otp


if __name__ == '__main__':
    print(f"Your otp: {generate_OTP()}")
