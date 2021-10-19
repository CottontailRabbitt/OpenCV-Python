import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("Binary", dst)

capture.release()
cv2.destroyAllWindows()
