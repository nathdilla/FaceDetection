import cv2


class Detect:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread('teens.jpg')

    username = None

    def __init__(self, username):
        Detect.username = username
        return

    @staticmethod
    def scan_image():
        num_of_faces = 0
        gray = cv2.cvtColor(Detect.img, cv2.COLOR_BGR2GRAY)
        faces = Detect.face_cascade.detectMultiScale(gray, 1.4, 4)
        for (x, y, w, h) in faces:
            num_of_faces = num_of_faces + 1
            cv2.rectangle(Detect.img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #cv2.imshow('img', img)
        #cv2.waitKey(0)

        print("Number of faces found: " + str(num_of_faces))

    @staticmethod
    def end_program():
        command = raw_input("Enter 'disconnect' to end session.")
        if command == "disconnect":
            cv2.destroyAllWindows()
            print("DISCONNECTED: " + Detect.username)
        else:
            Detect.end_program()


