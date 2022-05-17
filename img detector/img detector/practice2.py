import cv2
import glob        # glob (short for global) is used to return all file paths that match a specific pattern


Images = glob.glob("*.jpg")      # selecting all files that are .jpg

for image in Images:
    img = cv2.imread(image,0)
    re =cv2.resize(img,(100,100))
    cv2.imshow("Hey",re) 
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,re)



