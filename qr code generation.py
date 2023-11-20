#pip install pyqrcode
#pip install pypng
#pip install opencv
import cv2
import png
import pyqrcode
  
  
# String which represents the QR code
s = "BOSS HERE"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('qrcode.png', scale = 6)
qr_code=cv2.imread('qrcode.png')
cv2.imshow('qr code',qr_code)
