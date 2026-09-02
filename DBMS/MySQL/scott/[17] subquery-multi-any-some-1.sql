-- CHAPTER 07 서브쿼리(SUB QUERY)
-- 다중행 서브 쿼리: 쿼리 결과가 여러개의 행인 경우
-- IN, SOME, ANY, ALL, EXISTS

-- ANY, SOME
-- [ANY]
-- 서브 쿼리가 반환하는 각각의 값과 비교한다.
-- < ANY : 최대값보다 작으면 TRUE
-- > ANY : 최소값보다 크면 TRUE
-- = ANY : 범위안에 있는 값과 같으면 TRUE
-- <= ANY : 최대값보다 작거나 같으면 TRUE
-- >= ANY : 최소값보다 크거나 같으면 TRUE

USE scott;
SELECT sal FROM emp;

-- 직업('SALESMAN')인 사원의 급여
-- 최소값 : 1250
-- 최대값 : 1600
SELECT sal FROM emp WHERE job='SALESMAN' ORDER BY sal desc;

-- sal < ANY (...) : 최대값보다 작으면 TRUE
-- 직업('SALESMAN')인 사원의 급여 중 가장 급여를 많이 받는 사원보다
-- 급여를 작게 받는 사원
-- 급여가 sal < 1600인 경우
-- 서브쿼리의 결과 중 최대 보다 작은 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal < ANY (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal desc;
    
-- ANY, SOME을 쓰지 않고 처리: max
-- 급여가 sal < 1600인 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal < (SELECT max(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;
    
-- 서브쿼리의 결과 중 최소보다 큰 경우
-- 급여가 sal > 1250인 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal > ANY (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- min
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal > (SELECT min(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;
    
-- 각 부서별 최고 급여와 동일한 급여를 받는 사원
SELECT deptno, max(sal) FROM emp GROUP BY deptno; 
/*
10	5000.00
20	3000.00
30	2850.00
*/

-- ANY
SELECT empno, ename, job, deptno, sal
    FROM emp
    WHERE sal = ANY (SELECT max(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- SOME
SELECT empno, ename, job, deptno, sal
    FROM emp
    WHERE sal = SOME (SELECT max(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- SOME, ANY는 동일하다.
-- 서브쿼리의 결과 중 최소보다 큰 경우
-- 급여가 sal > 1250인 경우
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal > SOME (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- ANY, SOME을 쓰지 않고 처리
SELECT empno, ename, job, sal
    FROM emp
    WHERE sal > (SELECT min(sal) FROM emp WHERE job='SALESMAN')
    ORDER BY sal;

-- -------------------------------------------------------------
-- ANY
SELECT max(sal) FROM emp GROUP BY deptno; -- 5000, 3000, 2850

-- 부서별 최고 급여액과 동일한 급여를 받는 전체 사원
SELECT empno, ename, job, deptno, sal
    FROM emp
    WHERE sal = ANY (SELECT max(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- IN을 사용하여 위와 동일한 결과 도출
SELECT empno, ename, job, deptno, sal
    FROM emp
    WHERE sal IN (SELECT max(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- sal <= ANY (...) : 최대값보다 작거나 같으면 TRUE
-- 직업('SALESMAN')인 사원의 급여 중 가장 급여를 많이 받는 사원보다
-- 급여를 작거나 같은 사원
-- 급여가 sal <= 1600인 경우(이하)
-- 서브쿼리의 결과 중 최대 보다 작거나 같은 경우
SELECT sal FROM emp WHERE job='SALESMAN';

SELECT empno, ename, job, sal
    FROM emp
    WHERE sal <= ANY (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal desc;
    
-- sal >= ANY (...) : 최소값보다 크거나 같으면 TRUE
-- 직업('SALESMAN')인 사원의 급여 중 가장 급여를 적게 받는 사원보다
-- 급여를 크거나 같은 사원
-- 급여가 sal >= 1600인 경우(이하)
-- 서브쿼리의 결과 중 최초 보다 크거나 같은 경우
SELECT sal FROM emp WHERE job='SALESMAN';

SELECT empno, ename, job, sal
    FROM emp
    WHERE sal >= ANY (SELECT sal FROM emp WHERE job='SALESMAN')
    ORDER BY sal desc;    