import cv2
import numpy as np

src = np.zeros((480, 640, 3), dtype=np.uint8)

pts1 = np.array([[50, 50], [125, 150], [200, 50]])
pts2 = np.array([[250, 50], [325, 150], [400, 50]])
src = cv2.polylines(src, [pts1], True, (255, 0, 0), 3)
src = cv2.fillPoly(src, [pts2], (0, 255, 0), cv2.LINE_AA)

cv2.imshow("Polygon Draw", src)
cv2.waitKey()
cv2.destroyAllWindows()