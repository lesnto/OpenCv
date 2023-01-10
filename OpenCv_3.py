#from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import imutils

img1 = cv2.imread(filename='bear.jpg')
print(img1.shape)

gray = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray1 = cv2.threshold(src=gray, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]



#cv2.imwrite(filename='view-copy.jpg', img=M)
#cv2.imshow('window_name', gray)
cv2.imshow('window_name', gray1)


cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
