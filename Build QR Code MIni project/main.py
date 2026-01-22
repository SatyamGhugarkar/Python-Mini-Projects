'''
we are going to use the python libarary like QRcode and covert url to QR
'''
import qrcode
url = input("Enter the URL: ")
filename = input("Enter the filename to save it as : ")
if not filename.endswith('.png'):
    filename += '.png'

img = qrcode.make(url)
img.save(filename)