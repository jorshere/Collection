import cv2
from nbformat import read

img =cv2.imread("creta.jpg",0)

print(type(img))
#print(img)
print(img.shape)

cv2.imshow("myCar",img)

cv2.waitKey(0)     # the window will close when i press any key
cv2.waitKey(2000)            # window will close after given time i.e 2sec here;
cv2.destroyAllWindows()             # to destroy all windows


"""
for resized image;

resized_img = cv2.resize(img,(1000,500))
cv2.imshow("mycar2",resized_img)
cv2.waitKey(4000)
cv2.destroyAllWindows()
"""

resized_img1 = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("car1",resized_img1)
cv2.imwrite("creta_resize.jpg",resized_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


