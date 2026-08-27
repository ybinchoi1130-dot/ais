-- PRIMARY KEY: 메인키, 메인 인덱스

DROP TABLE IF EXISTS student2;

CREATE TABLE student2 (
	syear INT,          -- 입학년도
    sno   INT,          -- 입학순번
    name  VARCHAR(30),  -- 이름
    age   INT,          -- 나이
    email VARCHAR(30),  -- 전자메일
    PRIMARY KEY (syear, sno) -- 메인키(입학년도, 입학순번)
);

INSERT INTO student2 VALUES 
	(2000, 1, '일인자', 24, 'one@student.or.kr'),
	(2000, 2, '이인자', 24, 'two@student.or.kr'),
	(2000, 3, '삼인자', 24, 'three@student.or.kr'),
	(2001, 1, '사미자', 25, 'four@student.or.kr'),
	(2001, 2, '오미자', 26, 'five@student.or.kr');

SELECT * FROM student2;

-- 중복을 허용하지 않는 인덱스: email
CREATE UNIQUE INDEX uix_student2_email ON student2(email);

-- 인덱스 목록 확인
SHOW INDEX FROM student2;

-- 이메일 중복값 입력?
INSERT INTO student2 VALUES (2001, 3, '오미자', 26, 'five2@student.or.kr');

-- 오류: 이메일이 종복 되어서는 안된다.
-- Error Code: 1062. Duplicate entry 'five2@student.or.kr' for key 'student2.uix_student2_email'	0.000 sec
INSERT INTO student2 VALUES (2001, 4, '오징어', 27, 'five2@student.or.kr');

SELECT * FROM student2;

-- 인덱스 삭제
DROP INDEX uix_student2_email ON student2;
