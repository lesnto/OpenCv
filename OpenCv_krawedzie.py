#from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import imutils

img1 = cv2.imread(filename='python.png', flags=cv2.IMREAD_GRAYSCALE)
#print(img1.shape)

kernel_vertical = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
kernel_horizontal = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

#Output = cv2.filter2D(img1,ddepth=-1, kernel=kernel_horizontal)
Output=cv2.Canny(img1, threshold1=0, threshold2=0 )


cv2.imshow('window_name', Output)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
