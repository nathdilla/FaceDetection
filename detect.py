import cv2
from concurrent.futures import thread
import time

from pip._vendor.distlib.compat import raw_input


class Detect:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread('teens.jpg')

    username = None

    isActive = False
    connected = False

    def __init__(self, username):
        Detect.username = username
        Detect.connected = True
        return

    def scan_image(self, connection):
        try:
            print("Opening camera..")
            cap = cv2.VideoCapture(0)
            num_of_faces = 0

            while Detect.connected:
                _, img = cap.read()
                gray = cv2.cvtColor(Detect.img, cv2.COLOR_BGR2GRAY)
                faces = Detect.face_cascade.detectMultiScale(gray, 1.4, 4)
                for (x, y, w, h) in faces:
                    num_of_faces = num_of_faces + 1
                    cv2.rectangle(Detect.img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                cv2.imshow('img', img)
                if num_of_faces > 0:
                    Detect.isActive = True
                else:
                    Detect.isActive = False
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break

        except:
            print("Failure to open camera..")

        #print("Number of faces found: " + str(num_of_faces))

    @staticmethod
    def end_program():
        command = raw_input("Enter 'disconnect' to end session.")
        if command == "disconnect":
            cv2.destroyAllWindows()
            print("DISCONNECTED: " + Detect.username)
        else:
            Detect.end_program()


