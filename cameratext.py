import cv2
import pytesseract
from PIL import Image
videoObj = cv2.VideoCapture(0)
result = True
while result:
    cap, frame =videoObj.read()
    cv2.imshow('capturing',frame)
    if(cv2.waitKey(1)& 0xFF == ord('o')):
        cv2.imwrite('capture.jpg',frame)
        img =Image.open(r"C:\Users\Acer\Desktop\AI_ML\capture.jpg")
        pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(img)
        print(text)
        result =false
videoObj.release()
cv2.destroyAllWindows()
