import cv2
import numpy as np

src = np.zeros((480, 640, 3), dtype=np.uint8)

src = cv2.circle(src, (100, 100), 40, (255, 0, 0), -1)
src = cv2.circle(src, (200, 100), 40, (0, 255, 0), 3)

src = cv2.ellipse(src, (300, 100), (40,20), 0, 0, 360, (0, 0, 255), 3)
src = cv2.ellipse(src, (400, 100), (40,20), 45, 0, 360, (255, 255, 0), 3)
src = cv2.ellipse(src, (500, 100), (40,40), 0, 180, 360, (0, 255, 255), 3)

cv2.imshow("Circle Draw", src)
cv2.waitKey()
cv2.destroyAllWindows()