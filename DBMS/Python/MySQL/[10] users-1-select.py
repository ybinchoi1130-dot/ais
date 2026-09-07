# -*- coding: utf-8 -*-

# MySQL
# pip install mysqlclient

# 라이브러리 읽어 들이기
import MySQLdb

# MySQL 연결하기
conn = MySQLdb.connect(
    user='aisdb',
    passwd='aisdb',
    host='localhost',
    db='aisdb')

# 커서 추출하기
curr = conn.cursor()

try:
    # 데이터 추출하기
    sql = "SELECT * FROM users"
    curr.execute(sql)
    for row in curr.fetchall():
        print(row)
        
except Exception as e:
    print(f"DB 오류 발생: {e}")    
    conn.rollback();
    
finally:    
    curr.close()
    conn.close()
