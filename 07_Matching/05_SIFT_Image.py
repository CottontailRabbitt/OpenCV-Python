import numpy as np
import cv2


temp = cv2.imread('11_Samples/box.png',0)
scene = cv2.imread('11_Samples/box_in_scene.png',0)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(temp,None)
kp2, des2 = sift.detectAndCompute(scene,None)

bf = cv2.BFMatcher()

matches = bf.knnMatch(des1,des2, k=2)

good = []
for m,n in matches:
    if m.distance < 0.3*n.distance:
        good.append([m])
result = cv2.drawMatchesKnn(temp,kp1,scene,kp2,good,None,flags=2)

cv2.imshow('temp', temp)
cv2.imshow('scene', scene)
cv2.imshow('result', result)
cv2.waitKey(0)