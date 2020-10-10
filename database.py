import mysql.connector


class Database:
    meetingID = None
    mydb = None
    sqlFormula = "INSERT INTO users (username, classroomID, isActive, isTeacher) VALUES (%s, %s, %s, %s)"

    def __init__(self):
        Database.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="somesecurepassword",
            database="meetings"
        )

        print(Database.mydb)
        return

    def create_new_userconnection(self, username, code, isteacher):
        mycursor = Database.mydb.cursor()
        newuser = None

        if isteacher == 1:
            newuser = (username, code, 0, 1)
        else:
            newuser = (username, code, 0, 0) #check for existing code

        mycursor.execute(Database.sqlFormula, newuser)
        Database.mydb.commit()



