# qrcode generator
import qrcode

data = input('Input text or Url you wish to convert...').strip()
filename = input('which file should it be stored in? ').strip()

qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(data)
image = qr.make_image(fill_color='Black', back_color='White')
image.save(filename)
print(f'Qrcode saved in {filename}')