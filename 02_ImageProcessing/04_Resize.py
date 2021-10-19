import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    height, width, channel = frame.shape
    
    dst = frame[100:height-100, 200:width-200].copy()

    dst2 = frame.copy() 
    roi = frame[100:200, 150:300]
    dst2[0:100, 0:150] = roi

    cv2.imshow("Slice", dst)
    cv2.imshow("Paste", dst2)

capture.release()
cv2.destroyAllWindows()
