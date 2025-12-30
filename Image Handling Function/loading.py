import cv2

image = cv2.imread("D:\OpenCV\python_image.png")

if image is None:
    print("Error: Image is not found")
else:
    print("Image loaded successfully")