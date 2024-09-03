import cv2 as cv
face_cas=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0,cv.CAP_DSHOW)
while(True):
    ret,frame=cap.read()
    face=face_cas.detectMultiScale(frame,1.6,3)
    for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y,w,h),(255,0,0),3)
    cv.imshow("CAMERRA",frame)
    if cv.waitKey(1) &0XFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()