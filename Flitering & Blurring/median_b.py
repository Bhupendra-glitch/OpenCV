import cv2

image = cv2.imread("D:\OpenCV\Flitering & Blurring\Python.png")

blurred = cv2.medianBlur(image, 11)

cv2.imshow("Original Image", image)
cv2.imshow("Clean Image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()