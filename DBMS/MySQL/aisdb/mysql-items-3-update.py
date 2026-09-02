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
cur.execute('DROP TABLE IF EXISTS items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')
conn.commit()

#%%

# 데이터 추가하기 --- (※5)
datum = [('Banana', 300),('Mango', 640), ('Kiwi', 280), ('파인애플', 777)]
cur.executemany("INSERT INTO items(name,price) VALUES(%s,%s)", datum)
conn.commit()

#%%

# 데이터 추출하기 --- (※6)
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

#########################################################################
# 데이터 '가격', 변경하기 --- (※7)
# 주의: SQL문에 대응하는 값의 위치: 가격, 이름
print("변경된 가격")
datum = [(310, 'Banana'),(740, 'Mango'), (380, 'Kiwi'), (888, '파인애플')]
cur.executemany("UPDATE items set price=%s where name=%s", datum)
conn.commit()

# 데이터 추출하기 --- (※8)
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
