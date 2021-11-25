import numpy as np
import cv2


temp = cv2.imread('11_Samples/box.png',0)
scene = cv2.imread('11_Samples/box_in_scene.png',0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(temp,None)
kp2, des2 = orb.detectAndCompute(scene,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

matches = sorted(matches, key = lambda x:x.distance)

result = cv2.drawMatches(temp,kp1,scene,kp2,matches[:10],None,flags=2)

cv2.imshow('temp', temp)
cv2.imshow('scene', scene)
cv2.imshow('result', result)
cv2.waitKey(0)