import numpy as np, cv2, glob

# 영상 읽기 및 표시
img = cv2.imread("11_Samples/cup/image_0003.jpg")
cv2.imshow('query', img)

# 비교할 영상들이 있는 경로
search_dir = "11_Samples/cup"

# 이미지를 16X16 크기의 평균 해시로 변환하는 함수
def img2hash(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16, 16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi
 
# 해밍거리 측정 함수
def hamming_distance(a, b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)

    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a != b).sum()
    return distance

# 컵 영상의 해시 구하기
query_hash = img2hash(img)

# 이미지 데이터셋 디렉토리의 모든 영상 파일 경로
img_path = glob.glob(search_dir+'/*.jpg')

for path in img_path:

    # 데이터셋 영상 한개를 읽어서 표시
    img = cv2.imread(path)

    cv2.imshow('searching...', img)
    cv2.waitKey(2)  # 2ms간 대기

    # 데이터셋 영상 한 개의 해시
    a_hash = img2hash(img)

    # 해밍거리 산출
    dst = hamming_distance(query_hash, a_hash)

    if dst/256 < 0.2:  # 해밍거리 20% 이내만 출력 (80% 이상 닮은꼴)
        print(path, dst/256)
        cv2.imshow(path, img)

cv2.destroyWindow('searching...')
cv2.waitKey(0)
cv2.destroyAllWindows()