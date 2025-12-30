import cv2
image = cv2.imread("D:\OpenCV\Image Drawing Function\python_image.png")
if image is None:
    print("Oops! Your image is not working")
else:
    print("Image is Loaded Successfully!")

    resized = cv2.resize(image, (400, 400))

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite("resized_output.png", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()