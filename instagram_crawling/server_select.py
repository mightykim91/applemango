import mariadb
import sys
import json

# Connect to MariaDB Platform
try:
    # Get Cursor
    conn = mariadb.connect(
        host = "i3a503.p.ssafy.io",
        user = "root", 
        password = "mariadb",
        database = "subpjt2",
        # port=3306,
        )
    # print(conn) # 연결 확인용
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
cur = conn.cursor()

def SELECT(account):
    # DB와 python connect
    try:
        # ALTER TABLE TABLE_NAME CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        # sql = "SELECT * FROM instagrampictures"
        sql = "SELECT uinstagramid FROM userinfo WHERE uinstagramid = '" + ("%s" % account) + "'"
        # print(sql)
        cur.execute(sql)
        resultList = cur.fetchall()
        for res in resultList:
            print(res)
        # print(len(resultList))
        if len(resultList) > 0:
            return False
        else:
            return True
    except:
        print("SELECT 과정에서 에러 발생")
    conn.close()

# SELECT()