from itertools import count
from tkinter.messagebox import NO
import cv2, time            

first_frame =None

video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()                 # create first frame of window;
  #  
  #  print(check)            # true ie it is boolean; used for checking conditions
   # print(frame)               # it gives image in 3d matrix

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    grey = cv2.GaussianBlur(grey,(21,21),0)      # we want to blur the image, to remove noise amd for higher accuracy in img.
    # parameters:(img,blur ratio, gaussion standard deviation"zero")


    if first_frame is None:
        first_frame=grey
        continue

    delta_frame = cv2.absdiff(first_frame,grey)   # absdiff: abs difference give the difference between first frame and current frame 

   
    thresh_frame = cv2.threshold(delta_frame,30,255, cv2.THRESH_BINARY)[1]

    # it create a diffrence between first frame and delta frame,,, to detect motion; basically, it set limit to the pixils;
    # if it is more than 30; we can detect it as motion; 
    # it expect:(image,threshold limit,color assigh to value more then threshold limit(white),threshold method)[]
   
    thresh_frame = cv2.dilate(thresh_frame, None, iterations =7)
    #to remove the black hols from big white area OR to smoothen the threshold frame;

    # parameters: (frame,kernel array for sophisticated work,iteration for removing black holes in image)
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #finding contours of the moving objects; (using copy of the frame,retrieve only extreme outer contour, approximation
    #  method that openCV apply to retrieve the contours)


    for contour in cnts:                    # it find all the contours, then checks if the area is "less then 3000 pixel"
        if cv2.contourArea(contour)< 10000:    #we will ignore those pixils
            continue
        (x,y,w,h) = cv2.boundingRect(contour) #used to draw an approximate rectangle around the binary image
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)   #drawing rectangles;

    cv2.imshow("capturing",grey)
    cv2.imshow("delta frame",delta_frame)
    
    cv2.imshow("thresshold frame",thresh_frame)
    
    cv2.imshow("color img",frame)
    
    key = cv2.waitKey(1)
    print(grey)
    print(delta_frame)

    if key ==ord('q'):          # assign 'q' for quit the while loop;
        break

video.release()
cv2.destroyAllWindows()
