'''
__author__ = 'Song Chae Young'
__date__ = 'Dec.16, 2022'
__email__ = '0.0yeriel@gmail.com'
__fileName__ = 'image-crop.py'
__github__ = 'SongChaeYoung98'
__status__ = 'production'
'''

# 1

import os
import uuid
import cv2

VIDEO_FILE = 'data/FaceVideo_3x.mp4'  # The video file path to crop
IMAGES_PATH = os.path.join('data', 'images')  # Where the results will be saved.


def Rotate(src, degrees):  # Used when the video is rotated.
    if degrees == 90:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 1)

    elif degrees == 180:
        dst = cv2.flip(src, -1)

    elif degrees == 270:
        dst = cv2.transpose(src)
        dst = cv2.flip(dst, 0)

    else:  # up and down inversion
        dst = cv2.flip(src, degrees)

    return dst


cam = cv2.VideoCapture(VIDEO_FILE)  # WebCam = cv2.VideoCapture(CAM_ID)

width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

cv2.namedWindow('CAM_Window')

while (cam.isOpened()):
    ret, frame = cam.read()

    # Rotating the image(frame) 180 degree
    img = Rotate(frame, 180)

    # Rotated image
    # If you don't have to rotate, img -> frame
    cv2.imshow('CAM_Window', frame)

    # Capture images by frame
    # If you don't have to rotate, img -> frame
    print('Collecting image {}'.format(img))
    img_name = os.path.join(IMAGES_PATH, f'{str(uuid.uuid1())}.jpg')  # PNG is also possible (.jpg -> .png)
    cv2.imwrite(img_name, frame)

    if cv2.waitKey(1) >= 0:
        break

cam.release()
cv2.destroyWindow('CAM_Window')