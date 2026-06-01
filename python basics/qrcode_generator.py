import qrcode

url=input("Enter the link:").strip()
file_path="C:\\Users\\vkape\\OneDrive\\Desktop\\qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print('qr code is generated')