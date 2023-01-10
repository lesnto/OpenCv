#from google.colab.patches import cv2_imshow
import cv2

img1 = cv2.imread(filename='view.jpg')
print(img1.shape)

img2 = cv2.imread(filename='bear.jpg')
print(img2.shape)

add_img = cv2.add(src1=img1,src2=img2)

#img3 = cv2.imread(filename='view10.jpg', flags=cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(filename='view10.jpg')
print(img3)


dst = cv2.addWeighted(src1=img1, alpha=0.7,src2=img2, beta=0.3, gamma=0)

cv2.imshow('window_name', dst)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image


#cv2.imwrite(filename='view-copy.jpg', img=img1)


print('testy')