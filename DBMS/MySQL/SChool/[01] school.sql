
-- 데이터베이스 삭제
DROP DATABASE IF EXISTS school;

-- 데이터베이스 생성: scott
-- COLLATE utf8_general_ci: ci(Case Insensitive)
-- Case Insensitive: 
--   문자열 데이터 타입(VARCHAR, CHAR)
--   데이터베이스 엔진이 값을 비교할 때 대소문자를 같은 문자로 취급  
CREATE DATABASE school DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

SHOW databases;

USE school;

-- 전임교수
create table professor (
    profcd   char(4) primary key,
    name     varchar(30) not null
);

-- 전공학과
create table major (
	majorcd  char(3) primary key,   -- 전공학과코드
	name     varchar(30),  -- 전공학과이름
	profcd   char(4),               -- 전임교수
    constraint fk_major_profcd foreign key(profcd) references professor(profcd)
);

-- 과목목록
create table subjects (
	majorcd  char(3),                 -- 전공학과코드
    subcd    integer,                 -- 과목번호(자동 번호)
    name     varchar(30) not null,    -- 과목이름
    constraint pk_subjects primary key(majorcd, subcd),
    constraint fk_subjects_major_cd foreign key(majorcd) references major(majorcd)
);

-- 학생정보
create table student (
    studno   varchar(10) primary key,  -- 학번
    name     varchar(30) not null,     -- 이름
    majorcd  char(3),                  -- 전공학과코드
    telno    varchar(20),              -- 전화번호   
    email    varchar(30),              -- 전자메일
    constraint fk_student_majorcd foreign key(majorcd) references major(majorcd)
);


-- 전임교수
INSERT into professor values ('1010','최교수');
INSERT into professor values ('1020','박교수');
INSERT into professor values ('1030','이철영');

-- 전공학과
INSERT into major values ('100','컴공','1030');
INSERT into major values ('200','미술','1020');
INSERT into major values ('300','체육','1020');
INSERT into major values ('400','음악','1010');
INSERT into major values ('500','연기','1010');

select p.*,m.*
	from professor p join major m
    on p.profcd = m.profcd;
-- 교과 목록    
insert into subjects VALUES('100',1,'파이썬');
insert into subjects VALUES('100',2,'데이터베이스');
insert into subjects VALUES('100',3,'인공지능');

insert into subjects VALUES('500',1,'연극');
insert into subjects VALUES('500',2,'영화이론');
insert into subjects VALUES('500',3,'한국영화역사');

insert into subjects VALUES('300',1,'스포츠산업');
insert into subjects VALUES('300',2,'스포츠 재활의료');
insert into subjects VALUES('300',3,'축구');

-- 학생정보

INSERT into student values('260828','최정명','100',null,null);
INSERT into student values('260628','이지효','500',null,null);

select s.studno, s.name, s.majorcd, p.*, m.*
	from student s join major m on s. majorcd = m.majorcd
                        join professor p on m.profcd = p.profcd ;