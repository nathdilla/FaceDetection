import sys

sys.path.append(".")

from detect import Detect

username = None
password = None
classroomId = None
is_connected = False
is_teacher = False


def begin():
    global is_teacher
    global username
    global password
    global classroomId

    ask_is_teacher = raw_input("Enter 'T' for teacher.")
    if ask_is_teacher == "T":
        is_teacher = True
        print("Welcome, teacher")
    else:
        print("Welcome, student")
        is_teacher = False

    username = raw_input("Please enter your username: ")
    password = raw_input("Please enter your password: ")
    classroomId = raw_input("Please enter your current classroom code: ")
    print("Working..")
    if not is_teacher:
        face_detect = Detect(username).scan_image() #run this loop
        ##then sendDataToTeachers()
    else:
        print("Number of students")##loop check for students

    begin()
