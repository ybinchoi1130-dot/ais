# -*- coding: utf-8 -*-

# MySQL
# pip install mysqlclient

# 라이브러리 읽어 들이기 --- (※1)
import MySQLdb

# MySQL 연결하기 --- (※2)
conn = MySQLdb.connect(
    user='aisdb',
    passwd='aisdb',
    host='localhost',
    db='aisdb')

# 커서 추출하기 --- (※3)
cur = conn.cursor()


# 데이터 추출하기 --- (※6)
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
