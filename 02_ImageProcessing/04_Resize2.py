import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    height, width, channel = frame.shape
    dst2 = cv2.resize(frame, (320, 240))

    cv2.imshow("ori", frame)
    cv2.imshow("rezise", dst2)

capture.release()
cv2.destroyAllWindows()