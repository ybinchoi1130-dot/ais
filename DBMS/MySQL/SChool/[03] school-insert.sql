-- 전임교수
INSERT INTO professor VALUES ('1000', '공교수');
INSERT INTO professor VALUES ('1010', '이철영');
INSERT INTO professor VALUES ('1020', '최교수');

-- 전공학과
INSERT INTO major VALUES ('100', '컴공', '1000');
INSERT INTO major VALUES ('200', '영어', '1010');
INSERT INTO major VALUES ('300', '미술', '1020');
INSERT INTO major VALUES ('310', '음악', '1020');
INSERT INTO major VALUES ('320', '체육', '1020');

SELECT p.*, m.*
	FROM professor p JOIN major m
    ON p.profcd = m.profcd;
    
-- 과목목록    
INSERT INTO subjects VALUES ('100', 1, '파이썬');
INSERT INTO subjects VALUES ('100', 2, '데이터베이스');
INSERT INTO subjects VALUES ('100', 3, '인공지능');

INSERT INTO subjects VALUES ('300', 1, '서양미술');
INSERT INTO subjects VALUES ('310', 1, '바로크');
INSERT INTO subjects VALUES ('320', 1, '체육학개론');
INSERT INTO subjects VALUES ('320', 2, '경쟁심리학');

-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`school`.`subjects`, CONSTRAINT `fk_subjects_major_cd` FOREIGN KEY (`majorcd`) REFERENCES `major` (`majorcd`))	0.000 sec
INSERT INTO subjects VALUES ('400', 1, '사회학개론');

-- 학생정보
INSERT INTO student VALUES ('260828', '최정명', '100', NULL, NULL);
INSERT INTO student VALUES ('260829', '이지호', '320', NULL, NULL);

-- 학생의 전임교수이름, 전공학과이름
SELECT s.studno, s.name, s.majorcd,	p.*, m.*
	FROM student s, professor p, major m
    WHERE s.majorcd = m.majorcd
    AND m.profcd = p.profcd;
    
SELECT s.studno, s.name, s.majorcd,	p.*, m.*
	FROM student s 
    JOIN major m ON s.majorcd = m.majorcd
    JOIN professor p ON m.profcd = p.profcd;
    
SELECT s.studno, s.name, s.majorcd,	p.*, m.*
    FROM professor p 
    JOIN major m ON p.profcd = m.profcd
	JOIN student s ON s.majorcd = m.majorcd;
    
-- 학생의 전공 및 과목목록    
SELECT s.studno, s.name, s.majorcd,	m.*, j.*
	FROM student s, major m, subjects j
    WHERE s.majorcd = m.majorcd
    AND m.majorcd = j.majorcd;

SELECT s.studno, s.name, s.majorcd,	m.*, j.*
	FROM student s
    JOIN major m ON s.majorcd = m.majorcd
    JOIN subjects j ON m.majorcd = j.majorcd;

-- 전임교수에 속한 학생목록



