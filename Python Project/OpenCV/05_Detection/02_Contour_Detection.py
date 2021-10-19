import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

thr_min = 120
thr_max = 255

def on_thresold_min_change(pos):
    global thr_min
    thr_min = np.clip(pos, 0, 255)

def on_thresold_max_change(pos):
    global thr_max 
    thr_max = np.clip(pos, 0, 255)

cv2.namedWindow('Birary')


cv2.createTrackbar('thresold min', 'Birary', 1, 16, on_thresold_min_change)
cv2.createTrackbar('thresold max', 'Birary', 4, 16, on_thresold_max_change)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, thr_min, thr_max, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)

    #cv2.RETR_EXTERNAL : 외곽 윤곽선만 검출하며, 계층 구조를 구성하지 않습니다.  
    #cv2.RETR_LIST : 모든 윤곽선을 검출하며, 계층 구조를 구성하지 않습니다.
    #cv2.RETR_CCOMP : 모든 윤곽선을 검출하며, 계층 구조는 2단계로 구성합니다.
    #cv2.RETR_TREE : 모든 윤곽선을 검출하며, 계층 구조를 모두 형성합니다. (Tree 구조)

    #cv2.CHAIN_APPROX_NONE : 윤곽점들의 모든 점을 반환합니다.
    #cv2.CHAIN_APPROX_SIMPLE : 윤곽점들 단순화 수평, 수직 및 대각선 요소를 압축하고 끝점만 남겨 둡니다.
    #cv2.CHAIN_APPROX_TC89_L1 : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.
    #cv2.CHAIN_APPROX_TC89_KCOS : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for i in range(len(contours)):
        cv2.drawContours(frame, [contours[i]], 0, (0, 0, 255), 2)
        cv2.putText(frame, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
        #print(i, hierarchy[0][i])

    #cv2.namedWindow('grayimg')
    #cv2.imshow('grayimg', gray)
    #cv2.namedWindow('binimg')
    #cv2.imshow('binimg', binary)
    
    cv2.imshow('Birary', binary)
    cv2.imshow('Result', frame)



capture.release()
cv2.destroyAllWindows()