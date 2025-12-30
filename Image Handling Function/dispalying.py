import cv2

image = cv2.imread("D:\OpenCV\python_image.png")

if image is not None:
    cv2.imshow("Image showing", image) #open the window
    cv2.waitKey(0) #wait for a key press to close the window
    cv2.destroyAllWindows() #close the window
else:
    print("Could not load image")