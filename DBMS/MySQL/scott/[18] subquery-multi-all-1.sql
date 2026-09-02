-- CHAPTER 07 서브쿼리(SUB QUERY)
-- 다중행 서브 쿼리: 쿼리 결과가 여러개의 행인 경우
-- IN, SOME, ANY, ALL, EXISTS

-- ALL
-- 서브 쿼리에서 반환하는 모든 값과 비교
-- > ALL : 최대값보다 크면 TRUE
-- < ALL : 최소값보다 작으면 TRUE

USE scott;
SELECT min(sal) as min, max(sal) as max 
	FROM emp WHERE job='SALESMAN';   -- 1250, 1600

-- 급여가 sal > 1600보다 큰 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal > ALL (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- max(sal)    
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal > (SELECT max(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;
    
--------------------------------------------------------------------------------

SELECT min(sal) FROM emp WHERE job='SALESMAN';   -- 가장 작은 값: 1250


-- 서브쿼리의 결과에서 가장 작은 값보다 작은 행을 선택
-- 급여가 sal < 1250보다 작은 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal < ALL (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- 급여가 sal <= 1250보다 작은 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal <= ALL (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- min(sal)
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal < (SELECT min(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- 의미가 없음: 동일한 데이터
-- 권장하지 않음
-- 비효율적
SELECT sal FROM emp WHERE sal >= 5000;
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal = ALL (SELECT sal FROM emp WHERE sal >= 5000)
    ORDER BY sal;

-- ALL: 모든 결과가 만족해야 한다.
-- 급여가 3000 이상인 3000, 5000을 동시에 만족할 수 없다.
-- 그러므로 결과는 없다.
SELECT sal FROM emp WHERE sal >= 3000;
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal = ALL (SELECT sal FROM emp WHERE sal >= 3000)
    ORDER BY sal;

-- 급여가 sal >= 1600보다 크거나 같은 경우
-- MAX 함수로 처리하는 것을 권장
SELECT sal FROM emp WHERE job='SALESMAN'; -- 1250, 1600
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal >= ALL (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

SELECT empno, ename, job, sal
    FROM emp
    WHERE sal >= (SELECT max(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- 급여가 sal <= 1250보다 작거나 같은 경우
-- MIN 함수로 처리하는 것을 권장
SELECT sal FROM emp WHERE job='SALESMAN'; -- 1250, 1600
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal <= ALL (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

SELECT empno, ename, job, sal
    FROM emp
    WHERE sal <= (SELECT min(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;