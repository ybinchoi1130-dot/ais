use scott;

-- 테이블 정보
DESC dept2;

-- 테이블 이름: DEPT2
-- 메임 인덱스: PK_DEPT2(DEPTNO)
DROP TABLE IF EXISTS dept2;
CREATE TABLE DEPT2 (
    DEPTNO  INT PRIMARY KEY,
    DNAME   VARCHAR(15),
    LOC     VARCHAR(13)
);

DROP TABLE IF EXISTS dept2;
CREATE TABLE DEPT2 (
    DEPTNO  INT,
    DNAME   VARCHAR(15),
    LOC     VARCHAR(13),
    PRIMARY KEY (DEPTNO)
);

DROP TABLE IF EXISTS dept2;
CREATE TABLE DEPT2 (
    DEPTNO  INT,
    DNAME   VARCHAR(15),
    LOC     VARCHAR(13),
    CONSTRAINT PK_DEPT2 PRIMARY KEY (DEPTNO)
);

-- 기존 테이블을 이용해서 새로운 테이블 생성: 
-- 기본의 부서 테이블의 부서코드(10, 20, 30) 자료만 검색하여
-- 새로운 테이블 DEPT3로 생성
-- ※ 주의: 인덱스는 생성되지 않음
SELECT * FROM dept; -- 10, 20, 30, 40
DROP TABLE IF EXISTS dept3;
CREATE TABLE DEPT3
    AS SELECT * FROM DEPT WHERE DEPTNO IN (10, 20, 30);
    
DESC DEPT3;    
SELECT * FROM DEPT3;

-- Error Code: 1062. Duplicate entry '10' for key 'dept.PRIMARY'
INSERT INTO DEPT VALUES(10, '기획부', '대한민국');

-- 인덱스는 생성되지 않아 중복 데이터가 등록 됨
INSERT INTO DEPT3 VALUES(10, '기획부', '대한민국');
SELECT * FROM DEPT3;

-- 기존 테이블을 이용해서 새로운 테이블 생성할 때 구조만 복제
SELECT * FROM DEPT WHERE 0=1; -- 데이터가 0건이 검색

DROP TABLE IF EXISTS dept4;
CREATE TABLE DEPT4
    AS SELECT * FROM DEPT WHERE 0=1;    
DESC DEPT4;    
SELECT * FROM DEPT4;

-- 조건이 만족하지 않음으로 빈 데이터가 검색되어 구조만 만들어 지는 효과
DROP TABLE IF EXISTS dept5;
CREATE TABLE DEPT5
    AS SELECT * FROM DEPT WHERE 1 != 1;
DESC DEPT5;
SELECT * FROM DEPT5;

-- DELETE: 테이블 테이터만 삭제, Rollback(복구) 가능
-- TRUNCATE : 테이블의 테이터를 완전히 삭제, 구조는 삭제하지 않음
-- 롤백이 되지 않음
-- 롤백을 위한 백업을 하지 않기 때문에 처리 속도가 빠르다.
-- 테이블에 생성된 제약 조건과 인덱스, 뷰, 동의어는 유지
DROP TABLE IF EXISTS DEPTx;
CREATE TABLE DEPTx
    AS SELECT * FROM DEPT WHERE DEPTNO IN (10, 20, 30);
SELECT * FROM DEPTx;    -- 데이터 존재
TRUNCATE TABLE DEPTx;   -- 복구가 되지 않음
DESC DEPTx;             -- 테이블 구조 남아 있음
ROLLBACK;               -- 이전 작업을 복구
SELECT * FROM DEPTx;    -- 데이터가 없음, 복구되지 않음을 확인

-- DELETE : 테이블의 데이터만 삭제
-- 롤백이 되는 것이 TRUNCATE TABLE과 차이
DROP TABLE IF EXISTS DEPTx;
CREATE TABLE DEPTx AS SELECT * FROM DEPT;
    
SELECT * FROM DEPTx;    
DELETE FROM DEPTx;
ROLLBACK;
SELECT * FROM DEPTx;    

-- RENAME : 테이블 이름을 변경
-- RENAME TABLE 기존테이블 TO 새로운테이블;
RENAME TABLE DEPTx TO DEPTy;
DESC DEPTx; -- Error: Table 'scott.DEPT6' doesn't exist
DESC DEPTy;

-- 빈 테이블 생성: empx
CREATE TABLE empx
    AS SELECT * FROM emp WHERE 1 <> 1;

SELECT count(*) FROM empx;  -- 결과 : 0

-- [문제1]
-- 전체 사원(emp) 중에서 급여등급(salgrade)이 4등급인 사원 정보

-- [문제2]
-- 위의 문제1의 서브 쿼리를 하여 새로운 테이블에 입력
-- 서브 쿼리의 결과는 칼럼의 갯수와 자료형이 INSERT되는 테이블과 일치해야 한다.

-- [해설1]
SELECT * FROM salgrade; -- 4등급: 2001 ~ 3000
SELECT e.*, s.grade
    FROM emp e, salgrade s
    WHERE e.sal BETWEEN s.losal AND s.hisal
    AND s.grade = 4;

SELECT e.*, s.grade
    FROM emp e JOIN salgrade s
    ON e.sal BETWEEN s.losal AND s.hisal
    AND s.grade = 4;

-- [해설2]
INSERT INTO empx
    SELECT e.*
        FROM emp e, salgrade s
        WHERE e.sal BETWEEN s.losal AND s.hisal
        AND s.grade = 4;

SELECT * FROM empx;    

INSERT INTO empx
    SELECT e.*
        FROM emp e JOIN salgrade s
        ON e.sal BETWEEN s.losal AND s.hisal
        AND s.grade = 3;
    
SELECT * FROM empx;    

-- 서브 쿼리를 하여 자료를 입력할 때
-- 칼럼을 명시해서 칼럼의 갯수와 자료형을 맞출 수도 있다.
-- 지정되지 않은 컬럼의 내용은 NULL이 된다.
INSERT INTO empx (empno, ename, sal, deptno)
    SELECT e.empno, e.ename, e.sal, e.deptno
        FROM emp e, salgrade s
        WHERE e.sal BETWEEN s.losal AND s.hisal
        AND s.grade = 2;

-- 서브쿼리의 컬럼 갯수가 입력 되는 
-- 테이블의 갯수 보다 작으면 null로 처리할 수 있다.
INSERT INTO empx 
    SELECT e.empno, e.ename, null, null, null, e.sal, null, e.deptno
        FROM emp e, salgrade s
        WHERE e.sal BETWEEN s.losal AND s.hisal
        AND s.grade = 1;
        
SELECT * FROM empx;        




