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

# 데이터 추출하기 --- (※4)
cur.execute("SELECT * FROM items ORDER BY name")
resultset = cur.fetchall();

for row in resultset:
    print(type(row), row)      # tuple
    print(f"   [id] {row[0]}")
    print(f" [name] {row[1]}")
    print(f"[price] {row[2]}")
    print('-' * 20)    

# 작업단위 확정
conn.commit()

# 커서 닫기
cur.close()

# 접속 닫기
conn.close()
