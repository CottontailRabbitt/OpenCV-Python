import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
    laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
    canny = cv2.Canny(frame, 100, 255)

    cv2.imshow("Sobel", sobel)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)

capture.release()
cv2.destroyAllWindows()