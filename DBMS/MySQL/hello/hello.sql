-- 테이블 생성: hello
create table hello ( 
	hno int,          -- 정수형
    name varchar(30), -- 가변 문자열
    age integer       -- 정수형
);

-- 테이블 삭제
drop table hello;

-- 데이터 입력
INSERT INTO hello (hno, name, age) VALUES (1234, '홍길동', 34);
INSERT INTO hello (hno, name, age) VALUES (2000, '전우치', 27);
INSERT INTO hello (hno, name, age) VALUES (3000, '강감찬', 55);
INSERT INTO hello (hno, name, age) VALUES (4000, '사오정', 15);

-- 테이블의 컬럼(열)명을 생략 가능
INSERT INTO hello VALUES (5000, '오징어', 55);
INSERT INTO hello VALUES (7000, '행운아', null);
INSERT INTO hello VALUES (8000, '무일푼', 0);
INSERT INTO hello VALUES (9000, '0', 0);
INSERT INTO hello (name) VALUES ('이름만');

-- 전체 검색
SELECT * FROM hello;   

-- 조건 검색: WHERE 컬럼명 = 값
SELECT * FROM hello WHERE name = '이름만';
SELECT count(*) FROM hello WHERE name = '이름만';



-- 테이블의 전체 컬럼과 값목록(VALUES)과 일치 시켜야 한다.
INSERT INTO hello (hno, name) VALUES (6000, '육이오');
    
-- 검색    
SELECT * FROM hello;    

-- 데이터 전체 삭제: 되돌릴 수 없다.
TRUNCATE TABLE hello;
SELECT * FROM hello;    

INSERT INTO hello (hno, name, age) VALUES 
	(1234, '홍길동', 34),
	(2000, '전우치', 27),
	(3000, '강감찬', 55),
	(4000, '사오정', 15);
    
SELECT * FROM hello;    

-- 전체 데이터 삭제
DELETE FROM hello;