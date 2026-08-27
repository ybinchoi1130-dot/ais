-- 테이블을 삭제하면 테이블에 존재하는 모든 데이터가 삭제되고 테이블도 삭제 됨
-- 테이블이 존재 하면 테이블을 삭제
drop table if exists hello;

-- 테이블을 생성하며 유일한 하나만 존재해야 한다.
-- ※ 중복돼서 데이터가 입력될 수 있다.
CREATE TABLE hello (
	hno INT,
    name VARCHAR(30),
    age INTEGER
);

-- 입력: 테이블에 데이터를 입력
INSERT INTO hello (hno, name, age) VALUES (1111, '최정명', 22);

-- 입력: 동시에 여러 행을 입력
INSERT INTO hello (hno, name, age) VALUES 
	(1000, '홍길동', 34),
	(2000, '전우치', 27),
	(3000, '강감찬', 55),
	(4000, '사오정', 15);

-- 검색
SELECT * FROM hello;

-- 삭제: 컬럼(hno)가 숫자(1111)인 데이터
DELETE FROM hello WHERE hno = 1111;

-- 수정: 컬럼(hno)가 숫자(4000)인 '사오정' -> '손오공'
UPDATE hello SET name='손오공' WHERE hno=4000;