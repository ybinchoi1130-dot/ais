/*
MySQL에서 오라클(Oracle)과 동일하게 || 기호를 
문자열 연결 연산자로 사용하기 위한 설정

오라클과 MySQL의 차이점:

오라클(Oracle): || 기호를 두 문자열을 하나로 합치는 문자열 연결 연산자로 사용 
	(예: '안녕' || '하세요' ➔ '안녕하세요')

MySQL: 기본적으로 || 기호를 논리 연산자 OR의 의미로 사용하며, 
    문자열 연결에는 CONCAT() 함수를 사용

PIPES_AS_CONCAT 모드:

MySQL의 sql_mode에 PIPES_AS_CONCAT을 추가하면, 
MySQL에서도 || 기호를 오라클처럼 문자열 연결 연산자로 인식

코드 해석:

@@sql_mode: 현재 설정되어 있는 MySQL의 sql_mode 값들을 가져옴
CONCAT(@@sql_mode, ',PIPES_AS_CONCAT'): 기존 모드 설정값들의 맨 뒤에 ,PIPES_AS_CONCAT을 덧붙임
SET sql_mode=...: 변경된 값을 현재 세션의 sql_mode로 최종 적용
*/

SET sql_mode = CONCAT(@@sql_mode, ',PIPES_AS_CONCAT');
SELECT concat('안녕', '하세요') FROM DUAL;
SELECT '안녕' || '하세요' FROM DUAL;

-- 테이블 구조 변경: 
-- ALTER TABLE 테이블명 ADD COLUMN 칼럼명 자료형; : 칼럼 추가
-- ALTER TABLE 테이블명 RENAME COLUMN 기존칼럼명 TO 새로운칼럼명; : 칼럼 이름 변경
-- ALTER TABLE 테이블명 ALTER COLUMN 칼럼명 자료형; : 칼럼의 이름 변경 (MySQL 8.0.42부터 지원, 이전 버전에서는 RENAME COLUMN 사용)
-- ALTER TABLE 테이블명 MODIFY COLUMN 칼럼명 자료형; : 칼럼 자료형 변경
-- ALTER TABLE 테이블명 DROP COLUMN 칼럼명; : 칼럼 삭제

-- 제약조건 변경
-- ALTER TABLE 테이블명 ADD CONSTRAINT 제약조건명 제약조건; : 제약조건 추가
-- ALTER TABLE 테이블명 DROP CONSTRAINT 제약조건명; : 제약조건 삭제
-- ALTER TABLE 테이블명 MODIFY COLUMN 칼럼명 자료형 제약조건; : 제약조건 변경
-- ALTER TABLE 테이블명 ADD PRIMARY KEY(컬럼명); : 기본키 추가
-- ALTER TABLE 테이블명 DROP PRIMARY KEY; : 기본키 삭제
--------------------------------------------------------------------------------

-- 테이블 생성
DESC DEPTx;
DROP TABLE IF EXISTS DEPTx;

-- 테이블 이름: DEPTX
-- 메임 인덱스: PK_DEPTX(DEPTNO)
CREATE TABLE DEPTx (
    DEPTNO  INT, 
    DNAME   VARCHAR(15),
    LOC     VARCHAR(13),
    CONSTRAINT PK_DEPTX PRIMARY KEY(DEPTNO)
);

DROP TABLE IF EXISTS DEPTx;
CREATE TABLE DEPTX AS SELECT * FROM dept;
DESC DEPTx;
SELECT * FROM DEPTx;

-- 칼럼 추가(ADD)
-- 기존의 테이블에 자료이 있어서 기존의 자료를 유지할 필요가 있을 때
-- 테이블의 구조 변경
ALTER TABLE deptx ADD loc2 VARCHAR(50);

-- 칼럼 이름 변경(RENAME)
ALTER TABLE deptx RENAME COLUMN loc2 TO addr;
ALTER TABLE deptx RENAME COLUMN addr TO loc2;    -- 원상복귀

-- 칼럼 자료형 변경(MODIFY)
UPDATE deptx SET loc2 = loc || ', KOREA';
SELECT * FROM deptx;
SELECT loc2, length(loc2) FROM deptx;

-- loc2 VARCHAR(50) -> VARCHAR(10)
-- Oracle: ORA-01441: cannot decrease column length because some value is too big
-- MySQL: Error Code: 1265. Data truncated for column 'loc2' at row 1
-- 기존에 저장된 데이터보다 변경할 자료형의 길이 작으면 오류
ALTER TABLE deptx MODIFY loc2 VARCHAR(10);

SELECT max(LENGTH(loc2)) FROM deptx;   -- 최대 15바이트
ALTER TABLE deptx MODIFY COLUMN loc2 VARCHAR(15);
DESC deptx;

-- 칼럼 삭제
ALTER TABLE deptx DROP COLUMN loc2;

-- 칼럼 감추기(INVISIBLE) - MySQL 8.0.23 이상 (Oracle의 UNUSED 대안)
-- Oracle의 UNUSED는 완전히 접근 불가 상태로 만들지만, 
-- MySQL의 INVISIBLE은 SELECT * 결과에서만 제외됩니다.
ALTER TABLE deptx ADD addr VARCHAR(50);    -- 칼럼 추가
ALTER TABLE deptx ALTER COLUMN addr SET INVISIBLE; -- 칼럼 감추기 (보이지 않음)
desc deptx;          -- addr이 보이지만
SELECT * FROM deptx; -- addr이 보이지 않는다.

ALTER TABLE deptx DROP COLUMN addr;         -- INVISIBLE 상태에서도 삭제 가능 (정상 동작)
-- ALTER TABLE deptx MODIFY addr VARCHAR(30); -- 위에서 삭제했으므로 에러 발생: Error Code: 1054
ALTER TABLE deptx ADD addr VARCHAR(50);    -- 다시 사용을 위해 새로 추가

DESC deptx;
SELECT * FROM deptx;

UPDATE deptx SET addr = loc || ', KOREA';

-- 테이블(DEPTx)에 인덱스 추가
ALTER TABLE deptx
    ADD PRIMARY KEY (deptno);

-- 컬럼(addr)이 INVISIBLE로 설정되어 있기 때문에
-- all(*)로는 보이지 않아 명시적으로 지정
SELECT *, addr FROM deptx;

-- 위에서 메인키를 생성했으므로 중복키로 허용되지 않음
-- Error Code: 1062. Duplicate entry '10' for key 'deptx.PRIMARY'
INSERT INTO deptx (deptno, dname, loc, addr) 
	VALUES(10, 'RND', 'SEOUL', 'SEOUL, KOREA');

INSERT INTO deptx (deptno, dname, loc, addr) 
	VALUES(50, 'RND', 'SEOUL', 'SEOUL, KOREA');

SELECT *, addr FROM deptx;

-- 메인키 삭제
ALTER TABLE deptx
    DROP PRIMARY KEY;

ALTER TABLE deptx
    ADD CONSTRAINT pk_deptx PRIMARY KEY (deptno);

-- MySQL에서는 PRIMARY KEY 지정 시 제약조건 이름을 부여해도 항상 'PRIMARY'로 고정 됨
-- 따라서 DROP CONSTRAINT pk_deptx; 구문을 실행하면 해당 이름의 제약조건이 없어 에러(Error 3940)가 발생
-- PRIMARY KEY를 삭제할 때는 제약조건 이름 대신 항상 아래 구문을 사용해야 함
-- ALTER TABLE deptx DROP CONSTRAINT pk_deptx;

ALTER TABLE deptx
    DROP PRIMARY KEY;
    
-- PRIMARY KEY를 생성하지 않은 상태    
INSERT INTO deptx (deptno, dname, loc) VALUES(10, 'RND', 'SEOUL');

SELECT * FROM DEPTx; -- 중복키: 10

-- 테이블(DEPTx)에 인덱스 추가
-- Error Code: 1062. Duplicate entry '10' for key 'deptx.PRIMARY'
ALTER TABLE deptx ADD PRIMARY KEY (deptno);

DELETE FROM deptx WHERE dname = 'RND';      -- 중복 데이터 삭제
ALTER TABLE deptx ADD PRIMARY KEY (deptno); -- 성공
