-- 기존의 테이블을 사용하여 새로운 테이블을 생성

-- 검색 결과로 새로운 테이블을 생성(복사본)
CREATE TABLE emp2 AS SELECT * FROM emp;
SELECT * FROM emp2;

DROP TABLE emp2;
CREATE TABLE emp2 AS
	SELECT empno, 
		concat(left(ename, 1), lower(substring(ename, 2))) AS ename,
        job, mgr, hiredate, sal, comm, deptno
	FROM emp; 
    
SELECT * FROM emp2;

-- emp와 emp2는 서로 독립적인 테이블이다.
-- 그러므로 emp2에는 반영되지 않는다.
INSERT INTO emp 
	VALUES(9999, 'SOPIA', 'CLERK', 7902, '2020-10-10', 1600, NULL, 20);
SELECT * FROM emp WHERE empno = 9999;
SELECT * FROM emp2 WHERE empno = 9999;
