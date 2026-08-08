import qrcode

link = "https://github.com/TechbyC07"

qr = qrcode.QRCode(version=1)

qr.add_data(link)

qr.make(fit=True)

qr_image = qr.make_image(fill_color="Blue", back_color="White")

qr_image.save("generatedcode.png")