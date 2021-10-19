import cv2
import numpy as np

src = np.zeros((480, 640, 3), dtype=np.uint8)

src = cv2.rectangle(src, (50, 50), (100, 100), (255, 0, 0), -1)
src = cv2.rectangle(src, (150, 50), (200, 100), (0, 255, 0), 3)

cv2.imshow("Rectangle Draw", src)
cv2.waitKey()
cv2.destroyAllWindows()