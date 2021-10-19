import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Convert Color", dst)

capture.release()
cv2.destroyAllWindows()
