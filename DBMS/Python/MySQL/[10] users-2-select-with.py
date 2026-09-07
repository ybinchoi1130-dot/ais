# -*- coding: utf-8 -*-

# MySQL
# pip install mysqlclient

# 라이브러리 읽어 들이기
import MySQLdb

try:
    # MySQL 연결 (with 문: 예외 발생 시 자동 rollback, 정상 종료 시 commit)
    with MySQLdb.connect(
        user='aisdb',
        passwd='aisdb',
        host='localhost',
        db='aisdb') as conn:

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 추출하기
            sql = "SELECT * FROM users"
            curr.execute(sql)
            for row in curr.fetchall():
                print(row)

except Exception as e:
    print(f"DB 오류 발생: {e}")

