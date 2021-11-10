import cv2
import numpy as np

def on_blue_change(pos):
    global img # 밖에있는 img를 갖고 옴

    value = pos * 16 # 16 X 16 = 256 이므로 255가 아니라 0값으로 바뀜
    # value = np.clip(value, 0, 255) 넘파이에서 제공하는 함수를 이용해도 된다.

    if value >= 255: # 256일때 강제로 255로 변경
        value = 255

    img[:,:,0] = value
    cv2.imshow('image', img)

def on_red_change(pos):
    global img # 밖에있는 img를 갖고 옴

    value = pos * 16 # 16 X 16 = 256 이므로 255가 아니라 0값으로 바뀜
    # value = np.clip(value, 0, 255) 넘파이에서 제공하는 함수를 이용해도 된다.

    if value >= 255: # 256일때 강제로 255로 변경
        value = 255

    img[:,:,2] = value
    cv2.imshow('image', img)

def on_green_change(pos):
    global img # 밖에있는 img를 갖고 옴

    value = pos * 16 # 16 X 16 = 256 이므로 255가 아니라 0값으로 바뀜
    # value = np.clip(value, 0, 255) 넘파이에서 제공하는 함수를 이용해도 된다.

    if value >= 255: # 256일때 강제로 255로 변경
        value = 255

    img[:,:,1] = value
    cv2.imshow('Color TrackBar', img)

img = np.zeros((480,640,3), np.uint8)
cv2.namedWindow('image')

# 창이 생성된 이후에 호출해야 한다.
cv2.createTrackbar('Red', 'image', 0, 16, on_red_change)
cv2.createTrackbar('Green', 'image', 0, 16, on_green_change)
cv2.createTrackbar('Blue', 'image', 0, 16, on_blue_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()