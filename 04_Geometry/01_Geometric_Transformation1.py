import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    height, width, channel = frame.shape

    srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
    dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
    dst = cv2.warpPerspective(frame, matrix, (width, height))

    cv2.imshow("Geometic Transformation", dst)

capture.release()
cv2.destroyAllWindows()