import freenect
import cv2
import numpy as np

def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

def detect_circles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 50, param1=200, param2=30, minRadius=10, maxRadius=200)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]
            cv2.circle(frame, center, radius, (255, 0, 0), 3)
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
    return frame

def main():
    cv2.namedWindow('Hough Circles')
    while True:
        frame = get_video()
        output = detect_circles(frame)
        cv2.imshow('Hough Circles', output)
        if cv2.waitKey(1) == 27:  # Exit on ESC
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
