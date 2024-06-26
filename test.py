import cv2
import numpy as np
import freenect

kin  = cv2.VideoCapture(cv2.CAP_OPENNI)

ret,frame = kin.read()
print(ret)
print(frame)

# cv2.imshow('jaba',frame)