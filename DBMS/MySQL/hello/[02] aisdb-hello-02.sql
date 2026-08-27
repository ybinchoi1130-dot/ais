drop table if exists hello2;

-- 테이블을 생성하며 유일한 하나만 존재해야 한다.
-- ※ 컬럼에 PRIMARY KEY 옵션을 지정하면
--   중복해서 데이터를 입력할 수 없다.
-- 자료형
--   - INT, INTEGER: 정수형
--   - VARCHAR(30): 가변 문자열, 최대 30자리까지, 작은 따옴표 사용
CREATE TABLE hello2 (
	hno INT PRIMARY KEY, -- 메인 인덱스
    name VARCHAR(30),
    age INTEGER
);

-- 입력: 테이블에 데이터를 입력
INSERT INTO hello2 VALUES (1000, '홍길동', 34);
INSERT INTO hello2 VALUES (2000, '전우치', 27);
INSERT INTO hello2 VALUES (3000, '강감찬', 55);
INSERT INTO hello2 (hno, name, age) VALUES (4000, '사오정', 15);

-- 검색
SELECT * FROM hello2;

-- 중복해서 입력을 시도하면?
-- Error Code: 1062. Duplicate entry '1000' for key 'hello2.PRIMARY'
INSERT INTO hello2 VALUES (1000, '홍길동', 34);


-- 삭제: 컬럼(hno)가 숫자(1111)인 데이터
-- 존재하지 않는 데이터를 삭제하려고 하면?
-- 0 row(s) affected
-- 오류가 발생되지는 않지만 처리 건수가 0이다.
DELETE FROM hello2 WHERE hno = 1111;

-- 수정: 컬럼(hno)가 숫자(4000)인 '사오정' -> '손오공'
UPDATE hello2 SET name='손오공' WHERE hno=4000;

-- 여러 컬럼을 수정하려면
UPDATE hello2 
	SET name='저팔계', age=13
	WHERE hno=4000;

SELECT * FROM hello2 WHERE hno=4000;

-- OR: 둘 중에 하나라도 만족하는 레코드(행)
SELECT * FROM hello2 WHERE hno=1000 OR hno=4000;
SELECT * FROM hello2 WHERE hno=9000 OR hno=4000;

-- AND: 둘 다 모드 만족하는 레코드(행)
SELECT * FROM hello2 WHERE hno=4000 AND age=13; -- 저팔계
SELECT * FROM hello2 WHERE hno=4000 AND age=15; -- 없음

-- hno가 1000이거나 4000번인 것
-- IN은 OR 조건과 같다.
SELECT * FROM hello2 WHERE hno IN(1000, 4000);


