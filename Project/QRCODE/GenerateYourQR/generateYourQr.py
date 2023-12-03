import qrcode

print("In this program you will be able to generate your own QR code using url. Url format given below:")
print("Sample URL: https://instagram.com/your_User_Name\n")

userInput = input("Enter the Url: ")
qrCodeName = input("Enter name for qrcode: ")

qrCodeImg = qrcode.make(userInput)
qrCodeImg.save(qrCodeName + ".png")

print("QR Code saved successfully!")

print("\nThis QR Code generator has been developed by Mr. Mohammad Arsalan Rather")
input("Press any Enter key to exit. . . ")
