import cv2

image = cv2.imread("D:\OpenCV\python_image.png")

if image is not None:
    success  = cv2.imwrite("D:\OpenCV\saved_image.png", image)
    if success:
        print("Image saved successfully")
    else:
        print("Error in saving image")
else:
    print("Could not load image")

    