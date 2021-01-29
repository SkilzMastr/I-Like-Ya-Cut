import mysql.connector






def userInfo(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="deadMemes"
    )
    mycursor = db.cursor()
    mycursor.execute(f"SELECT `likes` FROM `cuts` where `userID`={id}")
    for x in mycursor:
        return x

def addUser(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="deadMemes"
    )
    mycursor = db.cursor()
    mycursor.execute(f'INSERT INTO `cuts` (userID, likes) VALUES ({id}, 1);')
    db.commit()
    return True


def addLike(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="deadMemes"
    )
    mycursor = db.cursor()
    mycursor.execute(f"UPDATE `cuts` SET `likes` = `likes` + 1 WHERE `userID` = {id}")
    db.commit()
    return True