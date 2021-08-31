import cv2
from easyocr import Reader
import re
import itertools


def cleanup_text(text):
    amount = re.findall(r'^[r|{]+[0-9]+$',text)
    str = ''.join(amount)
    return str

def implementOcr(img):
    image = cv2.imread(img)
    reader = Reader(['en'], True)
    results = reader.readtext(image)
    c = 0

    for bbox, text, prob in results:
        c += 1 
        superman = cleanup_text(text)
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        
        br = (int(br[0]), int(br[1]))
        
        bl = (int(bl[0]), int(bl[1]))

        if(len(superman)):
            print("[INFO] {}: {}".format(c, superman[1:]))
            cv2.rectangle(image, tl, br, (0, 255, 0), 2)
            cv2.putText(image, superman[1:], (tl[0], tl[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            return superman[1:],image

    
