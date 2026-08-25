create table hello (hno int, name varchar(30), age integer);
-- 검색
select * from hello;
-- 삭제
delete from hello where hno = 1000;
-- 중복돼서 데이터 입력될 수 있다. 
insert into hello(hno, name, age) values
		(1000,'손오공',19),
		(2000,'저팔계',21),
		(3000,'사오정',25),
		(4000,'삼장법사',16);
-- 수정
update hello set name = '손오공'  where hno = 4000;

create table hello2(
	hno int primary key,
    name varchar(25),
    age integer);
    
insert into hello2 values (5000, '홍길동', 27);

