drop table if exists student;

create table student (
syear int , -- 입학년도
sno int , -- 입학순번
name varchar(30),
age int,
primary key (syear, sno) -- 메인키(입학년도,입학순번)
);

insert into student values(2000,1,'일인자',20);
insert into student values(2000,2,'이인자',21);
insert into student values(2000,3,'삼인자',21);
insert into student values(2001,1,'사인자',20);
insert into student values(2001,2,'오인자',19);
insert into student values(2001,3,'육인자',19);

select * from student;

insert into student values(2000,1,'칠인자',22);

select * from student where syear =2000;
select * from student where syear =2001;

create index idx_student_age on student(age);
show index from student;

drop index idx_student_age on student;

-- 컬럼(age)의 값이 중복되는 행들이 존재하기 때문에 오류 발생
-- create unique index uix_student_age on student(age); -- key 가 충돌된다.
