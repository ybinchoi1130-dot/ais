-- filename: todos.sql

DROP TABLE IF EXISTS todo;
DROP TABLE IF EXISTS user;

-- 사용자 정보: user
CREATE TABLE user (
        id INTEGER NOT NULL AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL,
        hashed_password VARCHAR(255) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT (now()),
        PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_user_email ON user (email);

-- 해야할 일: todo
CREATE TABLE todo (
        id INTEGER NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        is_done BOOL NOT NULL,
        user_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES user (id)
)

