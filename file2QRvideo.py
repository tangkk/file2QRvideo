import base64
import sys
import qrcode
import cv2
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python file2QRvideo.py file video.avi") # video should be in avi format
        exit()

    file = sys.argv[1]
    video = sys.argv[2]

    fd = open(file, 'rb')
    blocksize = 600 # NOTE that this has to be multiples of 3

    bytes = fd.read(blocksize)
    img_array = []
    idx = 0
    framesize = None

    os.system("mkdir -p tmp/")
    prev_str = ""
    this_str = ""
    while bytes:
        this_str = base64.b64encode(bytes).decode("utf-8")
        if this_str == prev_str:
            print("this_str == prev_str!!")
            this_str += '?'
            prev_str = this_str

        img = qrcode.make(this_str)
        img.save("tmp/tmp-{}.png".format(idx))
        img = cv2.imread("tmp/tmp-{}.png".format(idx)) # convert PIL image to cv2 image
        height, width, layers = img.shape

        if framesize is None:
            framesize = (width, height)
        else:
            if (width, height) != framesize:
                img = cv2.resize(img, framesize)
        print(idx, img.shape)
        img_array.append(img)
        bytes = fd.read(blocksize)
        idx += 1

    # process remaining
    this_str = base64.b64encode(bytes).decode("utf-8")
    if this_str == prev_str:
        print("this_str == prev_str!!")
        this_str += '?'
        prev_str = this_str
    img = qrcode.make(this_str)
    img.save("tmp/tmp-{}.png".format(idx))
    img = cv2.imread("tmp/tmp-{}.png".format(idx))
    height, width, layers = img.shape
    if (width, height) != framesize:
        img = cv2.resize(img, framesize)
    print(idx, img.shape)
    img_array.append(img)

    # write out
    out = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*'DIVX'), 2, framesize)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
