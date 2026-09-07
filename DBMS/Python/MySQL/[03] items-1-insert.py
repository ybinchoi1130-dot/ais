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

# 테이블 생성하기 --- (※4)
# 데이터베이스 자료형
# VARCHAR(n) : 최대 길이 지정, 최대길이(65535), 속도 빠름
# TEXT: 길이 지정 불필요, 최대길이(65535), 속도 느림, 공간 효율, 인덱스 길이 지정 필요
cur.execute('DROP TABLE IF EXISTS items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')

# 데이터 추가하기 --- (※5)
datum = [('Banana', 300), ('Mango', 640), ('Kiwi', 280)]

# ProgrammingError: %d format: a real number is required, not bytes
# VALUES의 포맷을 (%d)로 하면 오류 발생
# cur.execute("INSERT INTO items(name,price) VALUES(%s,%d)", data)
# 포맷은 파라미터 마커(Parameter Marker)로서 무조건 %s를 사용한다.
# 데이터베이스 드라이버가 자동으로 타입에 맞게 처리한다.
for data in datum:
    # cur.execute("INSERT INTO items(name,price) VALUES(%s,%d)", data)
    cur.execute("INSERT INTO items(name, price) VALUES(%s,%s)", data)

# 데이터 추출하기 --- (※6)
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

cur.close()

conn.commit()
conn.close()
