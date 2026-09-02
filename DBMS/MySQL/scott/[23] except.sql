-- 집합연산자
-- 차집합(MINUS / EXCEPT)
-- A MINUS B (Oracle) / A EXCEPT B (Standard/MySQL 8.0.31+)
-- A의 검색 결과에서 B의 검색 결과를 뺀(제외한) 결과를 선택
-- MySQL 8.0.31 미만 버전에서는 EXCEPT 대신 NOT IN, NOT EXISTS 등을 사용해야 합니다.

-- 사원 정보에서 부서가 10이 아닌 사원 정보
SELECT * FROM emp WHERE deptno <> 10 ORDER BY deptno;

-- EXCEPT 대신 NOT IN 사용 (MySQL 하위 버전 호환)
SELECT * FROM emp 
WHERE empno NOT IN (SELECT empno FROM emp WHERE deptno = 10);

-- (MySQL 8.0.31 이상) EXCEPT 사용 예시
SELECT * FROM emp 
EXCEPT
SELECT * FROM emp WHERE deptno = 10;

-- 부서코드(10,20)을 제외하고 남은 부서
-- A EXCEPT B EXCEPT C -> NOT IN 사용
SELECT * FROM emp 
WHERE empno NOT IN (SELECT empno FROM emp WHERE deptno = 10)
  AND empno NOT IN (SELECT empno FROM emp WHERE deptno = 20);

-- UNION처럼 칼럼의 갯수가 일치해야 한다. (에러 발생 예시)
-- MySQL 8.0.31 이상에서 EXCEPT 사용 시 동일하게 컬럼 개수가 일치해야 합니다.
SELECT * FROM emp 
EXCEPT
SELECT job FROM emp WHERE job = 'SALESMAN';

-- 정상적인 EXCEPT 예시 (동일 컬럼)
SELECT job FROM emp 
WHERE job NOT IN (SELECT job FROM emp WHERE job = 'SALESMAN');

-- UNION과 NOT IN 복합 사용 예시
SELECT job, sal, deptno FROM emp
WHERE deptno NOT IN (30, 50)
UNION
SELECT job, sal, deptno FROM emp WHERE deptno IN (30, 50);
