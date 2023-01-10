#from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import imutils

img1 = cv2.imread(filename='python.png', flags=cv2.IMREAD_GRAYSCALE)
#print(img1.shape)

kernel = np.ones((5,5), np.uint8)
#Output=cv2.erode(img1, kernel=kernel,iterations=1)
Output=cv2.dilate(img1, kernel=kernel,iterations=1)

cv2.imshow('window_name', Output)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
