import cv2

#load cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

#capture video from webcam  
cap = cv2.VideoCapture(0)

while True:
    #read frame
    ret, frame = cap.read()
    #convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #draw rectangle around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    #display frame
    cv2.imshow('frame', frame)
    #wait for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
