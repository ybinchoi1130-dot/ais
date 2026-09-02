drop database if EXISTS school2;
create DATABASE school2;
use school2;

--  교수 테이블 
CREATE TABLE professors (
    prof_id VARCHAR(10) PRIMARY KEY,      -- 교번
    prof_name VARCHAR(30) NOT NULL,       -- 이름
    department VARCHAR(30) NOT NULL       -- 소속 학과
);

--  학생 테이블 
CREATE TABLE students (
    stu_id VARCHAR(10) PRIMARY KEY,       -- 학번
    stu_name VARCHAR(30) NOT NULL,        -- 이름
    major VARCHAR(30) NOT NULL,           -- 전공
    grade_year INT DEFAULT 1              -- 학년
);

-- 교과목 테이블 
CREATE TABLE class (
	class_id VARCHAR(4) PRIMARY KEY,     -- 강의 코드
	class_name VARCHAR(30) NOT NULL, -- 교과목
    prof_id VARCHAR(10) NOT NULL,    -- 담당교수
	FOREIGN KEY (prof_id) REFERENCES professors(prof_id)
);

-- 수강교과목 테이블
CREATE TABLE stu_class (
      class_id VARCHAR(4),
      semester VARCHAR(20),
      stu_id VARCHAR(10) NOT NULL,
      FOREIGN KEY (class_id) REFERENCES class(class_id),
	  FOREIGN KEY (stu_id) REFERENCES students(stu_id)
);




-- 교수 데이터
INSERT INTO professors VALUES ('P10',"김교수","인공지능학과");
INSERT INTO professors VALUES ('P20',"박교수","생명공학과");
INSERT INTO professors VALUES ('P30',"최교수","컴퓨터공학과");

-- 학생 데이터
INSERT INTO students VALUES ('S2601',"홍길동","컴퓨터공학과",1);
INSERT INTO students VALUES ('S2310',"아이어맨","인공지능학과",3);
INSERT INTO students VALUES ('S2602',"스파이더맨","생명공학과",1);
INSERT INTO students VALUES ('S2410',"헐크","생명공학과",3);
INSERT INTO students VALUES ('S2603',"슈퍼맨","컴퓨터공학과",1);
INSERT INTO students VALUES ('S2510',"배트맨","인공지능학과",2);
INSERT INTO students VALUES ('S2300',"전우치","인공공학과",3);

-- 교과목 데이터
INSERT INTO class VALUES ('C001',"CHAT_GPT",'P10');
INSERT INTO class VALUES ('C002',"DNA 탐구",'P20');
INSERT INTO class VALUES ('C003',"파이썬의 기초",'P30');

-- 수강교과 데이터 
INSERT INTO stu_class VALUES ('C001',"2026-1",'S2601');
INSERT INTO stu_class VALUES ('C001',"2026-1",'S2300');
INSERT INTO stu_class VALUES ('C001',"2026-1",'S2310');
INSERT INTO stu_class VALUES ('C001',"2026-1",'S2410');
INSERT INTO stu_class VALUES ('C001',"2026-1",'S2603');
INSERT INTO stu_class VALUES ('C002',"2026-1",'S2602');
INSERT INTO stu_class VALUES ('C002',"2026-1",'S2410');
INSERT INTO stu_class VALUES ('C003',"2026-1",'S2510');
INSERT INTO stu_class VALUES ('C003',"2026-1",'S2601');
INSERT INTO stu_class VALUES ('C003',"2026-1",'S2603');
INSERT INTO stu_class VALUES ('C003',"2026-1",'S2310');

SELECT 
    e.semester AS '학기',
    s.stu_name AS '학생명',
    c.class_name AS '수강 과목명',
    p.prof_name AS '담당 교수'
FROM stu_class e
INNER join students s ON e.stu_id = s.stu_id
inner JOIN class c ON e.class_id = c.class_id
inner JOIN professors p ON c.prof_id = p.prof_id;
