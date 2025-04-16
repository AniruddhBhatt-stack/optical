import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
Image_path='doouble.png'
reader = easyocr.Reader(['en'],gpu= False)
result = reader.readtext(Image_path)


img=cv2.imread(Image_path)
for detection in result:
    top_left=tuple([int(val) for val in detection[0][0]])
    bottom_right=tuple([int(val) for val in detection[0][2]])
    text=detection[1]
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),2)
    img=cv2.putText(img,text,top_left,font,0.5,(255,255,255),1,cv2.LINE_AA)
    print(text)
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()