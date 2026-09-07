# -*- coding: utf-8 -*-

# MySQL
# pip install mysqlclient

# 라이브러리 읽어 들이기
import MySQLdb

connect = {
    'user' : 'aisdb',
    'passwd' : 'aisdb',
    'host': 'localhost',
    'db' : 'aisdb'
}

query = {
    'columns' : ['id', 'name', 'postcd', 'postname'],
    'table': "userspost_vw",
    'sort': "name"
}

columns = ', '.join(query['columns']) # id, name, postcd, postname
sql = f"SELECT {columns} FROM {query['table']} ORDER BY {query['sort']}"
print(sql)

#%%

def print_users(records):
    print(columns)
    print('=' * 30)
    for record in records:
        for col in record:
            print(col, end=', ')
        print()

#%%
try:
    # MySQL 연결 (with 문: 예외 발생 시 자동 rollback, 정상 종료 시 commit)
    with MySQLdb.connect(
        user=connect['user'],
        passwd=connect['passwd'],
        host=connect['host'],
        db=connect['db']) as conn:

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 추출하기
            curr.execute(sql)
            print_users(curr.fetchall())

except Exception as e:
    print(f"DB 오류 발생: {e}")

