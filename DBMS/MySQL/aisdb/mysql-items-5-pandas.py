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
try:
conn.commit()

#%%

# 데이터 추가하기 --- (※5)
datum = [('Banana', 300),('Mango', 640), ('Kiwi', 280), ('파인애플', 777)]
cur.executemany("INSERT INTO items(name,price) VALUES(%s,%s)", datum)
conn.commit()

#%%

sql = "SELECT * FROM items"

# 데이터 추출하기 --- (※6)
cur.execute(sql)
for row in cur.fetchall():
    print(row)
###############################
# 데이터 삭제하기 ------(※7)
print("삭제된 데이터: Mango, 파인애플")
datum = [('Mango',),('파인애플',)]
cur.executemany("DELETE FROM items where name=%s",datum)
conn.commit()

cur.execute(sql)
for row in cur.fetchall():
    print(row)
except Exception as e:
    print(f"DB 오류 발생: {e}")
    conn.rollback();
finally:
    cur.close()
    conn.close()
#%%

import pandas as pd

items_df = pd.read_sql_query(sql, conn)
print(items_df)


#%%

conn.close()
