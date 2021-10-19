import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    
    range1 = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
    range2 = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
    rangedst = cv2.addWeighted(range1, 1.0, range2, 1.0, 0.0)
    hsvdst = cv2.bitwise_and(hsv, hsv, mask = rangedst)
    colordst = cv2.cvtColor(hsvdst, cv2.COLOR_HSV2BGR)

    cv2.imshow("HSV", hsv)
    cv2.imshow("hue", h)
    cv2.imshow("saturation", s)
    cv2.imshow("value", v)
    cv2.imshow("Masked HSV", colordst)

capture.release()
cv2.destroyAllWindows()