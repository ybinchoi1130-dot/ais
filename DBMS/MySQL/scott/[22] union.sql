-- 집합연산자(합집합)
-- 칼럼의 갯수와 자료형 일치
-- 충복되는 데이터는 하나만 선택
-- 
-- UNION ALL(합집합)
-- UNION과 동일하지만 중복을 포함 모든 결과를 리턴

USE scott;

-- 부서(10)에 속한 사원: 3명
SELECT * FROM emp WHERE deptno = 10;

-- 부서(20)에 속한 사원: 5명
SELECT * FROM emp WHERE deptno = 20;

-- 부서(10, 20)에 속한 사원: 8명
SELECT * FROM emp WHERE deptno IN(10,20) ORDER BY deptno;

-- 8명
SELECT count(*)
	FROM (SELECT * FROM emp WHERE deptno IN(10,20)) e;

-- UNION
SELECT * FROM emp WHERE deptno = 10 -- 부서(10)에 속한 사원
UNION
SELECT * FROM emp WHERE deptno = 20; -- 부서(20)에 속한 사원

-- 8명
SELECT COUNT(*)
	FROM (
		SELECT * FROM emp WHERE deptno = 10 -- 부서(10)에 속한 사원
		UNION
		SELECT * FROM emp WHERE deptno = 20  -- 부서(20)에 속한 사원
	) e;
    
-- 28건: 중복 허용    
SELECT count(*) FROM (SELECT * FROM emp UNION ALL SELECT * FROM emp) e;

-- 14건: 중복 제거
SELECT count(*) FROM (SELECT * FROM emp UNION SELECT * FROM emp) e;

-- UNION
SELECT deptno, dname, loc FROM dept; -- 10,20,30,40
SELECT CASE deptno 
        WHEN 10 THEN 10 + 1 
        WHEN 20 THEN 20 + 2 
        WHEN 30 THEN 30 + 3 
        WHEN 40 THEN 40 + 4 
        ELSE deptno 
       END AS dno, dname, loc FROM dept;

SELECT deptno, dname, loc FROM dept
UNION
SELECT CASE deptno 
        WHEN 10 THEN 10 + 1 
        WHEN 20 THEN 20 + 2 
        WHEN 30 THEN 30 + 3 
        WHEN 40 THEN 40 + 4 
        ELSE deptno 
       END AS dno, dname, loc FROM dept;

-- UNION ALL
SELECT * FROM emp WHERE deptno = 10 -- 부서(10)에 속한 사원: 3개
UNION ALL
SELECT * FROM emp WHERE deptno = 20 -- 부서(20)에 속한 사원: 5개
UNION ALL
SELECT * FROM emp WHERE deptno IN(10,20,30); -- 부서(10,20,30)에 속한 사원: 14개

-- A UNION B UNION ALL C
SELECT * FROM emp WHERE deptno = 10 -- 부서(10)에 속한 사원
UNION
SELECT * FROM emp WHERE deptno = 20 -- 부서(20)에 속한 사원
UNION ALL
SELECT * FROM emp WHERE deptno IN(10,20,30); -- 부서(10,20,30)에 속한 사원

-- 칼럼의 갯수가 일치 하지 않으면 에러
-- Error Code: 1222. The used SELECT statements have a different number of columns
SELECT * FROM dept 
UNION ALL 
SELECT * FROM emp;


