import cv2
import imutils
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
point_list = []

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    
    height, width, channel = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 75, 200)

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    
    cont = edged.copy()

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            cv2.drawContours(cont, [screenCnt], -1, (0, 0, 255), 2) 
            cv2.imshow("Outline", cont)

            dst = cont.copy()
            

            pts1 = np.float32([screenCnt[1],screenCnt[0],screenCnt[2],screenCnt[3]])
            pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

            M = cv2.getPerspectiveTransform(pts1,pts2)


            
            dst = cv2.warpPerspective(dst, M, (width,height))
            cv2.imshow("Resulit", dst)
            break

    
       
    
    
    
    
    cv2.imshow("Orignal Image", frame)
    cv2.imshow("Edge Image", edged)
    
 
    

capture.release()
cv2.destroyAllWindows()