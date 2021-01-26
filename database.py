import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='cut',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def addUser(id):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `users` (`userID`, `likes`) VALUES (%s, %s)"
            cursor.execute(sql, (id, '1'))
            result = cursor.fetchone()
        connection.commit()
        return result
    
def checkLikes(id):
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `likes` FROM `users` WHERE `userID`=%s"
            cursor.execute(sql, (id))
            result = cursor.fetchone()
            return result

def addLike(id):
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `users` SET `likes`=`likes`+1 WHERE `userID`=%s"
            cursor.execute(sql, (id))
            result = cursor.fetchone()
        connection.commit()
        return result