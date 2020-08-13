import cv2
import pytesseract
import imutils
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
image = cv2.imread('container_images/2.jpg')
image = image[50:150, 150:500] 
#cropping top right of the image where it is assumed that container number is written

# Display the original image
#cv2.imshow("Original Image", image)
#cv2.waitKey(0)

# RGB to Gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

'''
# ROI Selector
r = cv2.selectROI( gray )
width_start, height_start, width_end, height_end = r
cropped_img = gray[height_start: height_start + height_end, width_start: width_start + width_end]
cv2.imwrite( 'CroppedImage.jpg', cropped_img )  # Saving Cropped Image
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)  
'''
#Image Inverted
imagem = cv2.bitwise_not(gray)

#Bilateral Filtering
gray_new = cv2.bilateralFilter(imagem, 11, 17, 17)
print( "Container Number = " , pytesseract.image_to_string( gray_new )) # Try 1 (BEST RESULT IN MOST CASES)

#cv2.imshow("Bilateral Filter", gray_new )
#cv2.waitKey(0)
