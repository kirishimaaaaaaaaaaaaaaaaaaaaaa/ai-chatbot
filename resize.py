import cv2

image = cv2.imread('input.jpg')

size1 = (640, 480)
size2 = (800, 600)
size3 = (1024, 768)

resized1 = cv2.resize(image, size1)
resized2 = cv2.resize(image, size2)
resized3 = cv2.resize(image, size3)

cv2.imshow('Resized 640x480', resized1)
cv2.imshow('Resized 800x600', resized2)
cv2.imshow('Resized 1024x768', resized3)

cv2.imwrite('resized_640x480.jpg', resized1)
cv2.imwrite('resized_800x600.jpg', resized2)
cv2.imwrite('resized_1024x768.jpg', resized3)

cv2.waitKey(0)
cv2.destroyAllWindows()
