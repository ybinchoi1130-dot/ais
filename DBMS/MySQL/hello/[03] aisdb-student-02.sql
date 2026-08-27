-- PRIMARY KEY: 메인키, 메인 인덱스

DROP TABLE IF EXISTS student;

CREATE TABLE student (
	syear INT, -- 입학년도
    sno   INT, -- 입학순번
    name  VARCHAR(30),  -- 이름
    age   INT, -- 나이
    PRIMARY KEY (syear, sno) -- 메인키(입학년도, 입학순번)
);

INSERT INTO student VALUES 
	(2000, 1, '일인자', 24),
	(2000, 2, '이인자', 24),
	(2000, 3, '삼인자', 24),
	(2001, 1, '사미자', 25),
	(2001, 2, '오미자', 26);

SELECT * FROM student;

-- 새로운 인덱스 생성: 중복 허용(Non Unique)
-- 인덱스 이름   : idx_student_age
-- 인덱스 테이블 : student
-- 인덱스 컬럼   : age
CREATE INDEX idx_student_age ON student (age);

-- 인덱스 삭제
DROP INDEX idx_student_age ON student;

-- 중복을 허용하지 않는 UNIQUE 인덱스를 생성
-- Error Code: 1062. Duplicate entry '24' for key 'student.uix_student_age'	0.015 sec
-- 컬럼(age)의 값이 중복되는 행들이 존재하기 때문에 오류 발생
-- CREATE INDEX uix_student_age ON student(age);
-- DROP INDEX uix_student_age ON student;
CREATE UNIQUE INDEX uix_student_age ON student(age);

-- 인덱스 목록 확인
SHOW INDEX FROM student;
