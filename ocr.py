import numpy as np
import cv2
import pytesseract
import time
import threading
pytesseract.pytesseract.tesseract_cmd = 'D:\\python compiler\\tesseract.exe'
img = cv2.imread('ROI.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# LETTERS
# hImg, wImg = img.shape[:-1]
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, config=cong)
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(' ')
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]),int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,hImg-y), (w, hImg-h), (0,0,255), 1)
#     cv2.putText(img, b[0], (x,hImg-y+25), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


#WORDS
hImg, wImg = img.shape[:-1]
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config=cong)
for c,b in enumerate(boxes.splitlines()):
    if c != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]),int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,0,255), 1)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


cv2.imshow("result", img)
cv2.waitKey(0)