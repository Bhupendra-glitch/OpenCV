import cv2

image  = cv2.imread("D:\OpenCV\Image Drawing Function\python_image.png")

if image is None:
    print("Oops! Your image is not working")
else:
    print("Image loaded  successfully!")
    pt1 = (50, 50)
    pt2 = (200, 250)

    color = (0, 200, 0)
    thickness = 3

    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangle Drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()