#from google.colab.patches import cv2_imshow
import cv2

img1 = cv2.imread(filename='view.jpg')
print(img1.shape)
height, width, _ = img1.shape

h0 = height // 2 -100
h1 = height // 2 +100
w0 = width // 2 -100
w1 = width // 2 +100

#img1[h0:h1, w0:w1] = 81,82,82

person = img1[270:380, 260:320]
print(person.shape)

cv2.imwrite(filename='view-copy.jpg', img=person)

cv2.imshow('window_name', person)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
