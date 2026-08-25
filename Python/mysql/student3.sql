drop table if exists student2;

create table student2 (
syear int , -- 입학년도
sno int , -- 입학순번
name varchar(30),
age int,
email varchar(30),
primary key (syear, sno) -- 메인키(입학년도,입학순번)
);

insert into student2 values(2000,1,'일인자',20,'one@student.net');
insert into student2 values(2000,2,'이인자',21,'two@student.net');
insert into student2 values(2000,3,'삼인자',21,'three@student.net');
insert into student2 values(2001,1,'사인자',20,'four@student.net');
insert into student2 values(2001,2,'오인자',19,'five@student.net');
insert into student2 values(2001,3,'육인자',19,'six@student.net');

select * from student2;


create unique index uix_student_email on student2(email);
show index from student2;


-- 컬럼(age)의 값이 중복되는 행들이 존재하기 때문에 오류 발생
-- create unique index uix_student_age on student(age); -- key 가 충돌된다.
insert into student2 values(2002,1,'일순이',23,'one1@student.net');
insert into student2 values(2002,2,'이순이',22,'one1@student.net');