import qrcode

whatsApp_QR_img = qrcode.make("https://wa.me/917780880146")
whatsApp_QR_img.save("WhatsAppQrCode.png")

instagram_QR_img = qrcode.make("https://instagram.com/_.arsl_an")
img = instagram_QR_img.save("instagramQrCode.png")
