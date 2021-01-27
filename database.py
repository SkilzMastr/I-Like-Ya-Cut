import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='cut',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:

    def checkUser(id):
            with connection.cursor() as cursor:
                sql = "SELECT `likes` FROM `users` WHERE `userID`=%s"
                cursor.execute(sql, (id))
                result = cursor.fetchone()
                if result is None:
                    return addUser(id)
                else:
                    return result


    def addUser(id):
            with connection.cursor() as cursor:
                sql = "INSERT INTO `users` (`userID`, `likes`) VALUES (%s, %s)"
                cursor.execute(sql, (id, '1'))
            connection.commit()


print(checkUser('2'))