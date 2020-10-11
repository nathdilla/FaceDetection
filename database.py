import mysql.connector


class Database:
    meetingID = None
    mydb = None
    sqlFormula = "INSERT INTO users (username, classroomID, isActive, isTeacher) VALUES (%s, %s, %s, %s)" # user creation format

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
