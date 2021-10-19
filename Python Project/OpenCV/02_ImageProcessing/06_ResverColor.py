import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    dst = cv2.bitwise_not(frame)
    cv2.imshow("Reverse Color", dst)

capture.release()
cv2.destroyAllWindows()
