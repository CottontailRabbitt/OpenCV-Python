import cv2
import numpy as np

point_list = []
count = 0

def mouse_callback(event, x, y, flags, param):
    global point_list, count


    # 마우스 왼쪽 버튼 누를 때마다 좌표를 리스트에 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        print("(%d, %d)" % (x, y))
        point_list.append((x, y))

        print(point_list)
        cv2.circle(initimg, (x, y), 3, (0, 0, 255), -1)


capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while cv2.waitKey(32) < 0:
    ret, initimg = capture.read()
    height, width, channel = initimg.shape
    cv2.imshow("Initial", initimg)


cv2.namedWindow('Initial')
cv2.setMouseCallback('Initial', mouse_callback)



while cv2.waitKey(32) < 0:
    
    cv2.imshow("Initial", initimg)



# 좌표 순서 - 상단왼쪽 끝, 상단오른쪽 끝, 하단왼쪽 끝, 하단오른쪽 끝
pts1 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2]),list(point_list[3])])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

print("Input Point")
print(pts1)
print("Output Point")
print(pts2)

M = cv2.getPerspectiveTransform(pts1,pts2)

print("Perspective Transform Matrix")
print(M)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    height, width, channel = frame.shape
 
    dst = cv2.warpPerspective(frame, M, (width,height))

    cv2.imshow("Geometic Transformation", dst)

capture.release()
cv2.destroyAllWindows()