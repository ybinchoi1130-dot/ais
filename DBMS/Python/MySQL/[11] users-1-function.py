# -*- coding: utf-8 -*-

# MySQL
# pip install mysqlclient

# 유저 테이블 생성 SQL문
"""
CREATE TABLE users (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,         -- 이름
    age INTEGER(3) DEFAULT 0,          -- 나이
    email TEXT DEFAULT NULL,           -- 전자메일
    postcd CHAR(5) DEFAULT NULL,       -- 우편번호
    location VARCHAR(30) DEFAULT NULL, -- 상세주소
    -- 생성날짜: 생성시 현재 날짜로 자동 저장
    created_dt DATE DEFAULT (CURRENT_DATE), 
    -- 변경일시: 데이터 변경 시 현재 서버 타임존 시간으로 자동 갱신
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT CK_USERS_AGE CHECK (age BETWEEN 0 AND 100) -- 나이 범위 지정: 0 ~ 100
);
"""

# 라이브러리 읽어 들이기
import MySQLdb

# DB 접속
def connect_db():    
    try:
        # MySQL 연결
        conn = MySQLdb.connect(
            user='aisdb',
            passwd='aisdb',
            host='localhost',
            db='aisdb')
            
        return conn

    except Exception as e:
        print(f"DB 연결 오류 발생: {e}")


# DB 조회
def select_users(conn):    
    try:
        if not conn:
            return

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 추출하기
            sql = "SELECT * FROM users"
            curr.execute(sql)
            for row in curr.fetchall():
                print(row)

    except Exception as e:
        print(f"DB 조회 오류 발생: {e}")


# DB 추가
def insert_users(conn, name, age, email, postcd, location):    
    try:
        if not conn:
            return

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 추가하기
            sql = "INSERT INTO users (name, age, email, postcd, location) VALUES (%s, %s, %s, %s, %s)"
            curr.execute(sql, (name, age, email, postcd, location))
            conn.commit()
            print(f"데이터가 성공적으로 추가되었습니다: {curr.rowcount}")

    except Exception as e:
        print(f"DB 추가 오류 발생: {e}")

# DB 삭제
def delete_users(conn, name):    
    try:
        if not conn:
            return

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 삭제하기
            sql = "DELETE FROM users WHERE name = %s"
            curr.execute(sql, (name,))
            conn.commit()
            print(f"데이터가 성공적으로 삭제되었습니다: {curr.rowcount}")

    except Exception as e:
        print(f"DB 삭제 오류 발생: {e}")

# DB 모두 삭제
def delete_users_all(conn):    
    try:
        if not conn:
            return

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 삭제하기
            sql = "TRUNCATE TABLE users"
            curr.execute(sql, ())
            conn.commit()
            print(f"데이터가 성공적으로 삭제되었습니다: {curr.rowcount}")

    except Exception as e:
        print(f"DB 삭제 오류 발생: {e}")

# DB 수정
def update_users(conn, name, age, email, postcd, location):    
    try:
        if not conn:
            return

        # 커서 추출 (with 문: 블록을 벗어날 때 curr.close() 자동 호출)
        with conn.cursor() as curr:
            # 데이터 수정하기
            sql = "UPDATE users SET age = %s, email = %s, postcd = %s, location = %s WHERE name = %s"
            curr.execute(sql, (age, email, postcd, location, name))
            conn.commit()
            print(f"데이터가 성공적으로 수정되었습니다: {curr.rowcount}")

    except Exception as e:
        print(f"DB 수정 오류 발생: {e}")

if __name__ == "__main__":
    conn = connect_db()

    delete_users_all(conn)

    insert_users(conn, '이순신', 45, 'lss@abc.com', '12345', '충청도 서산')
    insert_users(conn, '유관순', 20, 'rgs@abc.com', '12345', '경기도 천안')
    insert_users(conn, '강감찬', 53, 'ggc@abc.com', '12345', '평안도 평양')

    delete_users(conn, '홍길동')
    delete_users(conn, '전우치')

    update_users(conn, '강감찬', 64, 'ggc@abc.com', '54321', '평안도 개성')
    select_users(conn)
    conn.close()


