import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


cv2.namedWindow('Result')

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    binary = cv2.bitwise_not(binary)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

    for contour in contours:
        epsilon = cv2.arcLength(contour, True) * 0.02
        approx_poly = cv2.approxPolyDP(contour, epsilon, True)

        for approx in approx_poly:
            cv2.circle(frame, tuple(approx[0]), 3, (255, 0, 0), -1)

    cv2.imshow('Binary', binary)
    cv2.imshow('Result', frame)



capture.release()
cv2.destroyAllWindows()