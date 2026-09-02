-- 집합 연산자 교집합(INTERSECT)
-- 동일한 데이터만 선택
-- 같은 데이터는 하나만 선택
-- 중복을 제거하는 효과
-- 한 쪽 테이블에만 있으면 선택되지 않음
-- MySQL 8.0.31 미만 버전에서는 INTERSECT 대신 IN 또는 INNER JOIN을 사용해야 합니다.

SELECT * FROM emp;
SELECT job, sal FROM emp ORDER BY 1,2;

-- 사원의 직업군 (MySQL 하위 버전 호환: IN 사용)
SELECT DISTINCT job FROM emp
	WHERE job IN (SELECT job FROM emp);

-- 사원들의 직책 목록: 중복제거 효과
-- (MySQL 8.0.31 이상) INTERSECT 사용 예시
SELECT job FROM emp
INTERSECT
SELECT job FROM emp;

-- 사원의 급여 목록 (MySQL 하위 버전 호환: IN 사용)
SELECT DISTINCT sal FROM emp
	WHERE sal IN (SELECT sal FROM emp)
    ORDER BY sal;

SELECT sal FROM emp
INTERSECT 
SELECT sal FROM emp
ORDER BY sal;

-- 사원의 급여 목록에서 관련된 사원 수
SELECT sal, count(sal) FROM emp GROUP BY sal ORDER BY 1;

-- 사원의 급여 목록
-- 양쪽 테이블에 급여가 같은 데이터가 없으므로 선택된 데이터가 없다.
SELECT DISTINCT sal FROM emp WHERE deptno = 10          -- 1300, 2450, 5000
  AND sal IN (SELECT sal FROM emp WHERE deptno = 20);   -- 800, 2975, 3000

-- 사원의 소속된 부서 10과 20에서 같은 급여를 받는 사원
-- 결과: 없다.
SELECT sal FROM emp WHERE deptno = 10
INTERSECT 
SELECT sal FROM emp WHERE deptno = 20;

-- [문제]
-- 각 부서별로 급여등급(salgrade)이 같은 사원 정보를 구하라.
-- 1단계: 교집합(INERSECT)을 이용하라.
-- 2단계: 기타 방법

-- 부서별 급여등급: 10:4-CLARK, 20:4-JONES, SCOTT, FORD
SELECT e.deptno, s.grade, e.empno, e.ename, e.sal
	FROM emp e
	JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
    AND e.deptno IN (10, 20)
    ORDER BY 1,2;

SELECT s.grade, e.deptno, e.empno, e.ename, e.sal
	FROM emp e
	JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
	WHERE e.deptno IN (10);

SELECT s.grade, e.deptno, e.empno, e.ename, e.sal
	FROM emp e
	JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
	WHERE e.deptno IN (20);

-- 1단계: 교집합(INTERSECT)을 이용 
-- (10번, 20번 부서에 공통으로 있는 급여 등급을 가진 사원)
SELECT s.grade, e.deptno, e.empno, e.ename, e.sal
FROM emp e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE s.grade IN (
    -- 10번 부서의 급여 등급
    SELECT s1.grade 
    FROM emp e1 JOIN salgrade s1 ON e1.sal BETWEEN s1.losal AND s1.hisal 
    WHERE e1.deptno = 10
    
    INTERSECT
    
    -- 20번 부서의 급여 등급
    SELECT s2.grade 
    FROM emp e2 JOIN salgrade s2 ON e2.sal BETWEEN s2.losal AND s2.hisal 
    WHERE e2.deptno = 20
)
AND e.deptno IN (10, 20)
ORDER BY s.grade, e.deptno;

-- 2단계: 기타 방법 (IN 연산자를 이용한 공통 급여 등급 추출)
SELECT s.grade, e.deptno, e.empno, e.ename, e.sal
FROM emp e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE s.grade IN (
    -- 10번 부서의 급여 등급 집합
    SELECT s1.grade 
    FROM emp e1 JOIN salgrade s1 ON e1.sal BETWEEN s1.losal AND s1.hisal 
    WHERE e1.deptno = 10
)
AND s.grade IN (
    -- 20번 부서의 급여 등급 집합
    SELECT s2.grade 
    FROM emp e2 JOIN salgrade s2 ON e2.sal BETWEEN s2.losal AND s2.hisal 
    WHERE e2.deptno = 20
)
AND e.deptno IN (10, 20)
ORDER BY s.grade, e.deptno;

-- 3단계: 기타 방법 (IN 연산자를 이용한 공통 급여 등급 추출)
SELECT s.grade, e.deptno, e.empno, e.ename, e.sal
FROM emp e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE s.grade IN (
    -- 10번 부서의 급여 등급 집합
    SELECT s1.grade 
    FROM emp e1 JOIN salgrade s1 ON e1.sal BETWEEN s1.losal AND s1.hisal 
    WHERE e1.deptno = 10
)
AND s.grade IN (
    -- 20번 부서의 급여 등급 집합
    SELECT s2.grade 
    FROM emp e2 JOIN salgrade s2 ON e2.sal BETWEEN s2.losal AND s2.hisal 
    WHERE e2.deptno = 20
)
AND e.deptno IN (10, 20)
ORDER BY s.grade, e.deptno;
