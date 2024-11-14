import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

image = cv2.imread('image.jpg')  

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

_, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

# Görüntüyü ekrana gösterin
cv2.imshow('Thresholded Image', thresh_image)

# Tesseract ile metin tanıma
extracted_text = pytesseract.image_to_string(thresh_image)

print("Tanınan Metin: ")
print(extracted_text)

# Görüntü üzerinde tanınan metni ekleyin
cv2.putText(image, extracted_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('El Yazisi Tanima', image)

cv2.imwrite('output_image.jpg', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
