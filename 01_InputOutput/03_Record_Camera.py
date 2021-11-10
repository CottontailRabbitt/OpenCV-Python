import datetime
import cv2
import os

runpath = os.path.dirname(os.path.abspath(__file__)) + "/"

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc(*'X264')

record = False

while True:
    ret, frame = capture.read()
    height, width, channel = frame.shape

    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == 27:
        break
    elif key == 26:
        print("캡쳐")
        cv2.imwrite(runpath + str(now) + ".png", frame)
    elif key == 24:
        print("녹화 시작")
        record = True
        
        #video = cv2.VideoWriter(os.getcwd() + "/" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        video = cv2.VideoWriter(runpath + str(now) + ".mp4", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 3:
        print("녹화 중지")
        record = False
        video.release()
        
    if record == True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()
