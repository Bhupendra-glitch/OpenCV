import cv2

image  = cv2.imread("D:\OpenCV\Image Drawing Function\python_image.png")    
if image is None:
    print("Oops! Your image is not working")
else:
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Original", rotated)
    cv2.imshow("Rotated 90 Degrees", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()