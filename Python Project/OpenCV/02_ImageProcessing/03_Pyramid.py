import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    height, width, channel = frame.shape

    dst = cv2.pyrUp(frame, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
    dst2 = cv2.pyrDown(frame)
    cv2.imshow("Pyramid UP", dst)
    cv2.imshow("Pyramid Down", dst2)

capture.release()
cv2.destroyAllWindows()
