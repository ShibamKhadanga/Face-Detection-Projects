# pip install opencv-python
#            OR
# pip install --upgrade opencv-python


import cv2


# Use file loaction where cv2 library is stored and search for face detection '.xml' file
''' Remember to change Back slash to Forward slash '''

face_cap = cv2.CascadeClassifier("C:/Users/DELL/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")



#Variable to enable camera
video_cap = cv2.VideoCapture(0)   



'''Open camera for permanent time'''
# this is used for infinite loop
while True :
    ret , video_data = video_cap.read() # detect face data using camera
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY) # Change face data color to grey for proper detection

    # Simply copy the under written code and paste it before writting code for rectangle or square on face 
    '''faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )'''

    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

    # Code to show Refctangle or shap[e on the face and the color of the shape
    for (x,y,h,w) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)


    # Code to show the video data or face data on the screen
    cv2.imshow("video_live",video_data)

    # Code to break the infinite loop by just pressing any key
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()  # release or show the captured data
