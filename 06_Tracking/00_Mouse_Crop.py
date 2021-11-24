import cv2
import numpy as np

import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0


def mouse_crop(event, x, y, flags, param):

    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start = x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
            
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:

        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        

        cropping = False # cropping is finished
        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2: #when two points were found
            roi = frame[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)

while cv2.waitKey(33) < 0:

    ret, frame = capture.read()
    cropped = frame.copy()

    if not cropping:
        cv2.imshow("image", frame)
    elif cropping:
        cv2.rectangle(cropped, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("image", cropped)

    cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()

