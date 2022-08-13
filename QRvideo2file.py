import cv2
import sys
from pyzbar.pyzbar import decode
import base64

# use
# ffmpeg -i <input> -filter:v fps=xxx <output>
# to change video to a lower framerate before processing

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: python QRvideo2file.py video file")
        exit()

    video = sys.argv[1]
    file = sys.argv[2]

    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()

    idx = 0

    resstr = ""
    prev_str = ""
    this_str = ""
    while success:
        decode_res = decode(image)
        if decode_res:
            print(idx, success, image.shape)
            this_str = decode_res[0].data.decode("utf-8")
            this_str = this_str.replace('?','')

            # dedup
            if this_str != prev_str:
                print("******{} newframe******".format(idx))
                resstr += this_str
                prev_str = this_str
            else:
                print("{} duplicate".format(idx))
        else:
            print("{} {} decoded empty!".format(idx, decode_res))

        success, image = vidcap.read()
        idx += 1

    # print(idx, success, image.shape)

    # process remaining
    if success:
        decode_res = decode(image)
        if decode_res:
            print(idx, image.shape)
            this_str = decode_res[0].data.decode("utf-8")
            this_str = this_str.replace('?', '')
            if this_str != prev_str:
                resstr += this_str
                prev_str = this_str

    bytearr = base64.b64decode(resstr)

    f = open(file, 'wb')
    f.write(bytearr)
    f.close()