####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################
from .models import Entery
f = []
for i in Entery.objects.all():
    f.append(i.face_id)

# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

import os 

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def return_id():

    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    assure_path_exists("trainer/")

    # Load the trained mode
    recognizer.read('/home/sem/Desktop/ATM/atm/app/trainer/trainer.yml')

    # Load prebuilt model for Frontal Face
    cascadePath = "/home/sem/Desktop/ATM/atm/app/haarcascade_frontalface_default.xml"
    cascadePath = "/home/sem/Desktop/ATM/atm/app/haarcascade_eye_tree_eyeglasses.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # Set the font style
    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'Ajay', 'Mahendra', 'Sunil ', 'Aayush', 'Aman'] 

    # Initialize and start the video frame capture
    cam = cv2.VideoCapture(0)

    # Loop
    while True:
        # Read the video frame
        ret, im =cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which ID
            Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidenceidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                print(Id)
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                # id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)

        # Display the video frame with the bounded rectangle
        cv2.imshow('show',im)


        # If 'q' is pressed, close program
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

        # if Id == 3:
        #     break

        # break
    cam.release()
    cv2.destroyAllWindows()
    return Id
# Stop the camera


# Close all windows
