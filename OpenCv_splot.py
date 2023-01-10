#from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import imutils

img1 = cv2.imread(filename='bear.jpg')
#print(img1.shape)

kernel = np.array([[-1,0,1],
                  [-5,0,5],
                  [-1,0,1]])
#imgSplot = cv2.filter2D(src=img1, ddepth=-1, kernel=kernel)
#imgSplot = cv2.blur(src=img1, ksize=(5, 5))
imgSplot = cv2.Laplacian(src=img1, ddepth=cv2.CV_64F)

print(kernel)

#cv2.imwrite(filename='view-copy.jpg', img=M)
#cv2.imshow('window_name', gray)
cv2.imshow('window_name', imgSplot)


cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
