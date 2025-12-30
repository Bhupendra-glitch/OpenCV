import cv2

cap =  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #ret - return true/false if frame is read correctly

    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #wait for 1 ms, if 'q' is pressed, break
        print("Quitting...")
        break

    cap.release()
    cv2.destroyAllWindows()

