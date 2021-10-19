import cv2
import numpy as np

src = np.zeros((480, 640, 3), dtype=np.uint8)

src = cv2.line(src, (50, 50), (50, 380), (0, 0, 255), 3)
src = cv2.line(src, (100, 50), (100, 380), (0, 255, 0), 3, cv2.LINE_4)
src = cv2.line(src, (150, 50), (150, 380), (255, 0, 0), 3, cv2.LINE_8)
src = cv2.line(src, (200, 50), (200, 380), (255, 255, 0), 3, cv2.LINE_AA)
src = cv2.arrowedLine(src, (250, 50), (250, 380), (0, 255, 255), thickness=3, tipLength=0.1)

cv2.imshow("Line Draw", src)
cv2.waitKey()
cv2.destroyAllWindows()