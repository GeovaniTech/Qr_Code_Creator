import qrcode

link = 'https://www.linkedin.com/in/geovani-debastiani/'

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=0
)

qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='transparent')
img.save('test.png')