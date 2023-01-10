#from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import imutils

img1 = cv2.imread(filename='bear.jpg')
#print(img1.shape)

imgRandom = np.random.randint(dtype=np.uint8, low=0,high=256, size=(400, 500, 3))
print(imgRandom)
print(imgRandom.dtype)

#cv2.imwrite(filename='view-copy.jpg', img=M)
#cv2.imshow('window_name', gray)

cv2.imshow('window_name', imgRandom)


cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
