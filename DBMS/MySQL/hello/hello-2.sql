-- 전체실행: Ctrl + Shift + Enter

-- 테이블이 존재 하면 테이블을 삭제
-- 테이블을 삭제하면 테이블에 존재하는 모든 데이터가 삭제되고 테이블도 삭제 됨
DROP TABLE IF EXISTS hello;
-- 테이블 생성: hello
create table hello ( 
	hno int,          -- 정수형
    name varchar(30), -- 가변 문자열
    age integer       -- 정수형
);
INSERT INTO hello (hno, name, age) VALUES 
	(1000, '홍길동', 34),
	(2000, '전우치', 27),
	(3000, '강감찬', 55),
	(4000, '사오정', 15);
SELECT * FROM hello;    
-- hno가 2000과 4000을 삭제
DELETE FROM hello WHERE hno IN (2000, 4000);
SELECT * FROM hello;    -- 남은 데이터는 : 1000, 3000
