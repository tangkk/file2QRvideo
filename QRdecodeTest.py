from kraken import binarization
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import cv2
from PIL import Image

image_path = "test.png"
# binarization using kraken
im = Image.open(image_path)
bw_im = binarization.nlbin(im)
# zbar
print(decode(bw_im, symbols=[ZBarSymbol.QRCODE]))


exit()

def binarization_cv2(im):
    blur = cv2.GaussianBlur(im, (5, 5), 0)
    ret, bw_im = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return bw_im

img = cv2.imread("test.png")
image = Image.open("test.png")
bw_img = binarization.nlbin(image)
# bw_img = binarization_cv2(img)

img2 = cv2.imread("tmp-0.png")

img = cv2.resize(img,(1330,1330))

decode_res = decode(img)
decode_res_bw_img = decode(bw_img, symbols=[ZBarSymbol.QRCODE])
decode_res2 = decode(img2)

print("decode_res:", decode_res)
print("decode_res_bw_img:", decode_res_bw_img)
print("decode_res2:", decode_res2)