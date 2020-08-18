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

# delete information
def DELETE():
    # sql = "DELETE FROM instagrampictures"
    print(sql)
    cur.execute(sql)
    conn.close()
# DELETE()