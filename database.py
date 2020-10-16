import mysql.connector


class Database:
    meetingID = None
    mydb = None
    sqlFormula = "INSERT INTO users (username, classroomID, isActive, isTeacher) VALUES (%s, %s, %s, %s)" # user creation format
    username = ""

    def __init__(self, username):
        Database.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="somesecurepassword",
            database="meetings"
        )

        print(Database.mydb)
        Database.username = username
        return

    def create_new_userconnection(self, username, code, isteacher):
        mycursor = Database.mydb.cursor()
        newuser = None

        if isteacher == 1:
            newuser = (username, code, 0, 1)
        else:
            sql = "SELECT * FROM users WHERE classroomID = %s"  # select all columns from users if classroomID equals code param
            mycursor.execute(sql, (code,))  # executes sql
            myresult = mycursor.fetchall()  # fetches results from previous execution. returns as table

            size = len(myresult)  # gets size of result
            if size > 0:  # if results are more than 0, then classroom must exists, if not, return false
                print("classroom exists!")
                newuser = (username, code, 0, 0)
            else:
                print("classroom does not exist!")
                return False

        mycursor.execute(Database.sqlFormula, newuser)
        Database.mydb.commit()
        return True

    def get_classroom_data(self, classroomID):
        mycursor = Database.mydb.cursor()
        sql = "SELECT username, isActive FROM users WHERE classroomId = %s"
        mycursor.execute(sql, (classroomID,))
        myresult = mycursor.fetchall()

        print("***********************")
        for user in myresult:
            print(user)

    def end_classroom(self, classroomID):
        mycursor = Database.mydb.cursor()
        sql = "DELETE FROM users WHERE classroomID = %s"
        mycursor.execute(sql, (classroomID,))
        Database.mydb.commit()

    def leave_classroom(self, username):
        mycursor = Database.mydb.cursor()
        sql = "DELETE FROM users WHERE username = %s"
        mycursor.execute(sql, (username,))
        Database.mydb.commit()

    def active_status(self, status):
        return
                #  set username status to status