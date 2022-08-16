import cv2
import numpy as np
img=cv2.imread("c.jpg")
cv2.imwrite("1.jpg",img)
print(img)
n,m,p=img.shape
img4=img
for i in range(150):
    img1=np.random.normal(0,10,(n,m,p))
    img4=img4+img+img1
img5=img4/150
cv2.imwrite("2.jpg",img1)
cv2.imwtite("3.jpg",img5)
