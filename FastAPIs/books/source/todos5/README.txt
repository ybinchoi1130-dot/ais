[README.txt]

# 터미널창에서 프로그램 실행
fastapi dev


-- 사용자 정보: user
DROP TABLE IF EXISTS user;
CREATE TABLE user (
        id INTEGER NOT NULL AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL,
        hashed_password VARCHAR(255) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT (now()),
        PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_user_email ON user (email);

-- 인덱스 확인
SHOW INDEX FROM user;
SHOW INDEXES FROM user;

-- 해야할 일: todo
DROP TABLE IF EXISTS todo;
CREATE TABLE todo (
        id INTEGER NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        is_done BOOL NOT NULL,
        user_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES user (id)
);

-- todo의 user_id를 null로 등록할 수 있지만
-- 값을 넣으면 user의 id가 있어야 한다.
insert into todo (title, is_done) values ('여행하기', false);     -- 정상등록
insert into todo (title, is_done, user_id) values ('관리하기', false, 1234); -- 오류
