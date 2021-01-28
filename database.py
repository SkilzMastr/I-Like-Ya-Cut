import mysql.connector






def userInfo(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="cut"
    )
    mycursor = db.cursor()
    mycursor.execute(f"SELECT `likes` FROM `users` where `userID`={id}")
    for x in mycursor:
        return x

def addUser(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="cut"
    )
    mycursor = db.cursor()
    mycursor.execute(f'INSERT INTO `users` (userID, likes) VALUES ({id}, 1);')
    db.commit()
    return True


def addLike(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="cut"
    )
    mycursor = db.cursor()
    mycursor.execute(f"UPDATE `users` SET `likes` = `likes` + 1 WHERE `userID` = {id}")
    db.commit()
    return True