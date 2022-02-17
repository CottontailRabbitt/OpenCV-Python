
import cv2 as cv
import sys
import os.path


prjpath = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
print(prjpath)

imgpath = prjpath + "\\11_Samples\starry_night.jpg"
print(imgpath)

img = cv.imread(imgpath)
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)