-- 사용자 정보
-- AUTO_INCREMENT: 
--   . 지정하지 않으면 데이터를 입력할 때 자동으로 1부터 1씩 증가하면서 부여(MAX + 1)
--   . 지정하면 지정된 값이 입력, 중복 가능성이 있음
-- DEFAULT: 데이터를 입력할 때 값을 지정하지 않으면 기본값

-- 테이블 삭제
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS postno;

-- 우편번호
CREATE TABLE postno (
	postcd CHAR(5) PRIMARY KEY, -- 우편번호
    postname VARCHAR(50)        -- 주소
);

INSERT INTO postno VALUES('00000', '이름없는 거리');
INSERT INTO postno VALUES('11111', '기술의 거리');
INSERT INTO postno VALUES('12345', '알수없는 거리');
INSERT INTO postno VALUES('54321', '갈수없는 거리');
INSERT INTO postno VALUES('99999', '잊혀진 거리');
SELECT * FROM postno;
COMMIT;

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
    CONSTRAINT CK_USERS_AGE CHECK (age BETWEEN 0 AND 100), -- 나이 범위 지정: 0 ~ 100
    CONSTRAINT FK_USERS_POSTCD FOREIGN KEY(postcd) REFERENCES postno(postcd)
);
    
INSERT INTO users (name, age, email, postcd) VALUES 
	('김홍수', 45, 'khs@abc.com', '11111'),
	('홍길동', 34, 'hgd@abc.com', '12345'),
	('전우치', 27, 'jwc@abc.com', '54321'),
	('임꺽정', 45, 'lgj@abc.com', '99999');

INSERT INTO users (id, name, age, email, postcd, created_dt, updated_at) VALUES 
	(99, '비둘기', 3, 'gg@abc.com', '99999', '2026-08-31', '2026-08-31 10:15:20');

INSERT INTO users (name, age, email, postcd) 
	VALUES ('강아지', 7, 'dog@abc.com', '00000');

-- 우편번호가 없기 때문에 입력되지 않음
-- INSERT INTO users (name, age, email, postcd) 
-- 		VALUES ('고양이', 3, 'dog@abc.com', '77777');
    
SELECT * FROM users;    

UPDATE users SET age = 8 WHERE name = '강아지';

-- Error Code: 3819. Check constraint 'CK_USERS_AGE' is violated.
-- UPDATE users SET age = -1 WHERE name = '강아지';
-- UPDATE users SET age = 101 WHERE name = '강아지';

COMMIT;

-- 조인(JOIN) : users, postno
SELECT * FROM postno;
SELECT u.*, p.*
	FROM users u JOIN postno p
    ON u.postcd = p.postcd;

-- 뷰(VIEW)
CREATE OR REPLACE VIEW userspost_vw AS
	SELECT u.*, p.postname
		FROM users u JOIN postno p
		ON u.postcd = p.postcd;

SELECT * FROM userspost_vw;