import cv2
import numpy as np

image = cv2.imread("D:\OpenCV\Flitering & Blurring\Python.png")

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpen_kernel = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow("Original Image", image)
cv2.imshow("sharpened Image", sharpen_kernel)
cv2.waitKey(0)
cv2.destroyAllWindows()