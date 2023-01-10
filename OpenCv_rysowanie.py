#from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import imutils

img1 = cv2.imread(filename='bear.jpg')
#, flags=cv2.IMREAD_GRAYSCALE

copy = img1.copy()

cv2.imshow('window_name', cv2.rectangle(img=copy, pt1=(75,80), pt2=(180,200), color=(0,0,255), thickness=2 ))
cv2.imshow('window_name', cv2.circle(img=copy, center=(300,300), radius=30, color=(0,0,255), thickness=-1 ))
cv2.imshow('window_name', cv2.line(img=copy, pt1=(75,80), pt2=(180,200), color=(0,0,255), thickness=1 ))
cv2.imshow('window_name', cv2.putText(img=copy, text="test", org=(10,40), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1.5, color=(0,0,255), thickness=2 ))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
