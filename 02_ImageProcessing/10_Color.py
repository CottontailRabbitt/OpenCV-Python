import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    b, g, r = cv2.split(frame)
    dst = cv2.merge((b, r, g))


    cv2.imshow("Original", frame)
    cv2.imshow("Convert Color", dst)
    #cv2.imshow("Blue", b)
    #cv2.imshow("Green", g)
    #cv2.imshow("Red", r)

capture.release()
cv2.destroyAllWindows()