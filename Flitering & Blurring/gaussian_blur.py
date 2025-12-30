import cv2

image = cv2.imread("D:\OpenCV\Flitering & Blurring\Python.png")

blurred =  cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Original Image", image)
cv2.imshow("gaussian Blurred image", blurred)

cv2.waitKey(0)
cv2.destoryedAlliWindows()
