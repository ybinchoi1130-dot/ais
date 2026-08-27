-- PRIMARY KEY: 메인키, 메인 인덱스

DROP TABLE IF EXISTS student;

-- 오류발생
-- Error Code 1068: Multiple primary key defined
/*
CREATE TABLE student (
	syear INT PRIMARY KEY, -- 입학년도
    sno   INT PRIMARY KEY, -- 입학순번
    name  VARCHAR(30),  -- 이름
    age   INT -- 나이
);
*/

CREATE TABLE student (
	syear INT, -- 입학년도
    sno   INT, -- 입학순번
    name  VARCHAR(30),  -- 이름
    age   INT, -- 나이
    PRIMARY KEY (syear, sno) -- 메인키(입학년도, 입학순번)
);

INSERT INTO student VALUES (2000, 1, '일인자', 24);
INSERT INTO student VALUES (2000, 2, '이인자', 24);
INSERT INTO student VALUES (2000, 3, '삼인자', 24);
INSERT INTO student VALUES (2001, 1, '사미자', 25);
INSERT INTO student VALUES (2001, 2, '오미자', 26);

-- 중복 시험: 
-- Error Code: 1062. Duplicate entry '2000-1' for key 'student.PRIMARY'	0.000 sec
-- 입력이 되지 않음: PRIMARY KEY 충돌(중복)
-- 입학년도와 순번을 결합해서 중복이 되면 안된다.
INSERT INTO student VALUES (2000, 1, '우등생', 23);

-- '일인자'만 존재한다.
SELECT * FROM student WHERE syear = 2000 AND sno = 1;

-- 2000년에 입학한 학생 목록
SELECT * FROM student WHERE syear = 2000;

-- 2001년에 입학한 학생 목록
SELECT * FROM student WHERE syear = 2001;
