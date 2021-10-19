import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    dst = cv2.blur(frame, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

    cv2.imshow("Blur", dst)

capture.release()
cv2.destroyAllWindows()
