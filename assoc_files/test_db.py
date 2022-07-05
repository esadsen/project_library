import mysql.connector
import db
from assoc_files.model import User



try:
    connection = mysql.connector.connect(host='database-server-instance-1.cp3fdruwvi5c.us-east-1.rds.amazonaws.com',
                                         database='db_server',
                                         user = 'admin',
                                         password = 'fehmimustafa')
    print(connection.is_connected())
    print("connected")
    sql = "SELECT * FROM db_server.users"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total => ", cursor.rowcount)
    print("each row")
    for row in result:
        print(row)
    

    user = User.query.all()
    print(user)
except:
    print('not connected')
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("closed")