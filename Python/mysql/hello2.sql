-- "컬럼 primary key 옵션을 지정하면 중복해서 데이터를 입력할 수 없다.
-- varchar(?): 가변 문자열, 최대 (?)자리까지, 작은 따옴표 사용
create table hello2(
	hno int primary key, -- 메인 인덱스
    name varchar(25),
    age integer);
 
 select * from hello2;
 select * from hello2 where hno=8000 or hno=5000;
select * from hello2 where hno = 8000 or age = 25;
-- in은 or 조건과 같다.
select * from hello2 where hno in(5000,6000);
 select * from hello2 where hno=6000 and age = 42;
 select * from hello2 where hno=6000 and age = 40; -- 없음

insert into hello2 values (5000, '홍길동', 27);
insert into hello2 values (6000, '전우치', 29);
insert into hello2 values (8000, '스파이더맨', 25);
update hello2
	set name =('헐크'),
    age = (42)
    where hno = (6000);