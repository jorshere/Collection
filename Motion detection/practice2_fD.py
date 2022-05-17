import cv2, time              #used for img and video processing;

"""
video = cv2.VideoCapture("movie.mp4")         

 # method trigger video captures;
 # # if you have video in computer then you can pass path;
 or you can pass index of camera with you want to capture
 """
a=0
video = cv2.VideoCapture(0)

while True:
    a=a+1               # it will add the times while loop runs; it no of frame we have
    check, frame = video.read()                 # create first frame of window;
    
    print(check)            # true ie it is boolean; used for checking conditions
    print(frame)               # it gives image in 3d matrix

    #grey = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)

    #time.sleep(3)



    cv2.imshow("capturing",frame)

    key = cv2.waitKey(2)

    #cv2.waitKey(2000)
    if key ==ord('q'):          # assign 'q' for quit the while loop;
        break

print(a)
video.release()
cv2.destroyAllWindows()
