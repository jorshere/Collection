from turtle import shape
import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")      # create a face _case object

"""this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, "photo.jpg")
"""
img = cv2.imread("news.jpg")

"""
1) its better to use grey scale as it gives more accuracy"""

grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     # conver BGR img to grey scale



"""faces = face_cascade.detectMultiScale(grey_img,        #it will detect upper left corner of the face in the image and
scaleFactor = 1.05,                         # width and height of rectangle definingthe face in img
minNeighbors=5)"""

faces = face_cascade.detectMultiScale(grey_img,        #it will detect upper left corner of the face in the image and
scaleFactor = 1.05,                         # width and height of rectangle definingthe face in img
minNeighbors=5)


"""
print(type(faces))         # <class 'numpy.ndarray'>
print(faces)                #[[157  84 379 379]]  gives the face coordinates;"""


for p,q,r,s in faces:
    img = cv2.rectangle(img, (p,q),(p+r,q+s),(0,255,0),3)     # passed arg:(img,(first and last coordinates),RGB color,width of rectangle)



print(type(faces))         # <class 'numpy.ndarray'>
print(faces)                #[[157  84 379 379]]  gives the face coordinates;


resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Grey",img)

cv2.waitKey(0)
cv2.destroyAllWindows()



