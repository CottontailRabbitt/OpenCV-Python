import cv2
import numpy as np
# 설치 : pip3 install pillow
from PIL import ImageFont, ImageDraw, Image

src = np.zeros((480, 640, 3), dtype=np.uint8)

b,g,r,a = 0,255,0,0

# Windows
# fontpath = "fonts/gulim.ttc"  

# Mac
fontpath = "/Library/Fonts/AppleSDGothicNeo.ttc"
font = ImageFont.truetype(fontpath, 20)
img_pil = Image.fromarray(src)
draw = ImageDraw.Draw(img_pil)
draw.text((100, 100),  "한글입력", font=font, fill=(b,g,r,a))
src = np.array(img_pil)

cv2.putText(src,  "putText", (200,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b,g,r), 1, cv2.LINE_AA)




cv2.imshow("Text Draw", src)
cv2.waitKey()
cv2.destroyAllWindows()