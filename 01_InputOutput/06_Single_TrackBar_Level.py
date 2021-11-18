import cv2
import numpy as np
def on_level_change(pos):
    global img # 밖에있는 img를 갖고 옴

    value = pos * 16 # 16 X 16 = 256 이므로 255가 아니라 0값으로 바뀜
    # value = np.clip(value, 0, 255) 넘파이에서 제공하는 함수를 이용해도 된다.

    if value >= 255: # 256일때 강제로 255로 변경
        value = 255

    img[:] = value
    cv2.imshow('Level TrackBar', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')

# 창이 생성된 이후에 호출해야 한다.
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()